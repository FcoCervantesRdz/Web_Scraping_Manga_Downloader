import requests
import shutil
import os
from PIL import Image
from bs4 import BeautifulSoup
main_page = 'https://ww5.manganelo.tv/'

# Needed functions
def int_to_str(num:int, num_digits:int):
    """This function return a string number from an integer number
    and a specific number of digits. For example:
    >>> int_to_str(12,4)
    '0012'
    >>> int_to_str(1,5)
    '00001'"""
    if type(num) != int:
        raise TypeError("num has to be an integer")
    elif type(num_digits) != int:
        raise TypeError("num_digits has to be an integer")
    elif len(str(num)) > num_digits:
        raise ValueError("num_digits has to be bigger or equal than the number of digits of num")
    elif len(str(num)) == num_digits:
        return str(num)
    else:
        return '0'*(num_digits-len(str(num))) + str(num)

def convert_proper_name(name):
    name = name.replace(' ','_')
    not_allowed_char = ['<','>',':','"','/','\\','|','?','*']
    for char in not_allowed_char:
        name = name.replace(char,'')
    return name

def clean_imgs():
    "This function delets all the imgs saved in 'temp_imgs'"
    try:
        shutil.rmtree('./temp_imgs')
        os.mkdir('./temp_imgs/')
        return
    except:
        return

def clean_mangas():
    "This function delets all mangas saved in 'mangas'"
    try:
        shutil.rmtree('./mangas')
        os.mkdir('./mangas')
        return
    except:
        return


def get_chapters_elements(manga_code:str):
    global main_page
    """This function returns al list of the 'a' elements that contains all information
    about the chapters (name and link)"""
    if type(manga_code) != str:
        raise TypeError('"manga_code" must be a string')

    manga_url = main_page + 'manga/manga-'+manga_code
    # Get the chapters
    manga_r = requests.get(manga_url)
    if manga_r.status_code == 200: # If our requests was succesful
        manga_html = BeautifulSoup(manga_r.content, 'html.parser')
        return list(manga_html.find_all('a', class_='chapter-name text-nowrap'))
    else:
        #Check if we have internet:
        if requests.get('http://google.com').status_code != 200:
            raise ConnectionError('There is not connection to internet')
        else:
            raise ValueError('There is not connection using that value of "manga_code"')

def select_chapters_elements(chapters_elements:list):
    """This function takes the list of all chapters elements and ask the user of those 
    he/she wants to download. It returns these selected chapters elements on a list."""
    if type(chapters_elements) != list:
        raise TypeError('"chapters_elements" must be a list.')
    elif len(chapters_elements) == 0:
        raise ValueError('"chapters_elements" must have at least one element')
    return chapters_elements[0:1] # This will be develop on streamlit functions

def download_image(img_url:str, img_name:str):
    if type(img_url) != str:
        raise TypeError('"img_url" must be a string.')
    elif not '.' in img_url:
        raise ValueError('"img_url" must have at least one dot "." on it.') 
    elif type(img_name) !=str:
        raise TypeError('"img_name" must be a string.')
    
    img_ext = img_url.split('.')[-1]
    img_r = requests.get(img_url)
    if img_r.status_code == 200:
        img_content = img_r.content # Get img
        path = './temp_imgs/'+img_name+'.'+img_ext
        with open(path, 'wb') as handler:
            handler.write(img_content)
        return path
    else:
        #Check if we have internet:
        if requests.get('http://google.com').status_code != 200:
            raise ConnectionError('There is not connection to internet')
        else:
            raise ValueError('There is not connection using that img_url:'+img_url)        

def create_PDF(manga_code:str, chapter_name:str, imgs_paths:list):
    if type(manga_code)!=str:
        raise TypeError('"manga_code" must be a string.')
    elif type(chapter_name)!=str:
        raise TypeError('"chapter_name" must be a string.')
    elif type(imgs_paths)!=list:
        raise TypeError('"imgs_paths" must be a list.')
    elif len(imgs_paths)<=1:
        raise ValueError('"imgs_paths" must have at least two elements.')
    imgs_list = [Image.open(path).convert('RGB') for path in imgs_paths[1:]]
    pdf_path = './mangas/'+manga_code+'-'+chapter_name+'.pdf'
    if os.path.isfile(pdf_path):
        os.remove(pdf_path)
    Image.open(imgs_paths[0]).convert('RGB').save(pdf_path, save_all=True, append_images=imgs_list)
    return pdf_path

def download_selected_chapters(selected_chapters_elements:list, manga_code:str):
    """This function download all selected chapters"""
    global main_page
    if type(selected_chapters_elements)!= list:
        raise TypeError('"selected_chapters_elements" must be a list')
    elif len(selected_chapters_elements) == 0:
        raise ValueError('"selected_chapters_elements" must have at least one element')
    chapters_paths = []
    for chapter_element in selected_chapters_elements:
        chapter_url = main_page + chapter_element['href']
        chapter_r = requests.get(chapter_url) #Get into chapter's page
        if chapter_r.status_code == 200:
            chapter_html = BeautifulSoup(chapter_r.content, 'html.parser')
            clean_imgs()
            #Get all images in chapter
            imgs_elements = chapter_html.find_all('img', class_='img-loading') 
            num_pages = len(imgs_elements)
            num_digits = len(str(num_pages))
            counter = 0
            imgs_paths = []
            for img_element in imgs_elements:
                img_url = img_element['data-src'] # Get url 
                img_name = int_to_str(counter, num_digits) # for example: '001.jpg'
                path = download_image(img_url,img_name)
                imgs_paths.append(path)
                counter += 1
            chapter_name = convert_proper_name(chapter_element.text)
            chapters_paths.append(create_PDF(manga_code, chapter_name, imgs_paths))
            clean_imgs()

    return chapters_paths