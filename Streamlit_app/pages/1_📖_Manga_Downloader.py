import streamlit as st
from functions import *

st.set_page_config(
    page_title="Manga Downloader", 
    page_icon="📖"
)

st.markdown('# Manga Downloader 📘')
st.markdown("""To find a code, search in [Manganelo](https://ww5.manganelo.tv/),
            if you want to try an example, you can use 'ne990439'""")
clean_imgs()
manga_search = st.text_input("Search for any manga:", placeholder='Example: Beyond the sky')
col0_1, col0_2 = st.columns(2)

chapters_elements = []
chapters_names = []
selected_chapters_name = []
manga_code = ''
name = ''
if manga_search != '':
    searched_elements = search(manga_search)
        # Get manga from the user
    if not searched_elements is None and len(searched_elements)!=0:
        names = [element.text for element in searched_elements]
        with col0_1:
            name = st.selectbox('Choose one', names)
    else:
        with col0_1:
            st.error('Try another search')

if name != '':
    selected_element = [element for element in searched_elements if element.text == name][0]
    manga_code = selected_element['href'].split('-')[-1]

if manga_code != '':
    try:
        chapters_elements = get_chapters_elements(manga_code)
    except ValueError:
        with col0_1:
            st.error("It looks that's not a correct manga code, check the section 'FAQ' for more information.")

# Get the chapters from the user
if len(chapters_elements) != 0:
    chapters_names = [chapter_element.text for chapter_element in chapters_elements]
    chapters_names.reverse()
    with col0_2:
        bool_chapters_selected = st.checkbox('Chapters selected...')
    with col0_1:
        selected_chapters_name = st.multiselect(
            'Select the chapters you want to download:',
            chapters_names,
            disabled=bool_chapters_selected)
        if bool_chapters_selected:
            if len(selected_chapters_name) == 0:
                st.error('Select at least one chapther...')
            else:
                selected_chapters_elements = [selected_chapter for selected_chapter in chapters_elements if selected_chapter.text in selected_chapters_name]

# Downloading
if len(selected_chapters_name) != 0 and bool_chapters_selected:
    with col0_2:
        downloaded = True
        chapter_paths = []
        for chapter_element in selected_chapters_elements:
            if not os.path.exists('./mangas/'+manga_code+'-'+convert_proper_name(chapter_element.text)+'.pdf'):
                downloaded = False
                chapter_paths = []
                break
            chapter_paths.append('./mangas/'+manga_code+'-'+convert_proper_name(chapter_element.text)+'.pdf')
        if not downloaded:
            space_chapbar = st.empty()
            space_pagebar = st.empty()
            chapters_bar = space_chapbar.progress(0.0, text="Converting chapters to PDF...")
            pages_bar = space_pagebar.progress(0.0, "Getting pages from Manganelo...")
            chapter_paths = download_selected_chapters(selected_chapters_elements, manga_code, chapters_bar, pages_bar)
            space_chapbar.empty()
            space_pagebar.empty()
        st.success('The chapters have been succesfully Converted!')
        for chapter_path in chapter_paths:
            file_name = chapter_path.split('/')[-1]
            with open(chapter_path,'rb') as file:
                st.download_button(
                    label="Download "+file_name,
                    data=file,
                    file_name=file_name,
                )

