import streamlit as st
from functions import *

st.set_page_config(
    page_title="Manga Downloader", 
    page_icon="📖"
)

st.markdown('# Manga Downloader 📘')
chapters_elements = []
chapters_names = []
selected_chapters_name = []
col0_1, col0_2 = st.columns(2)

def find_manga():
    global chapters_names, chapters_elements, col0_1, col0_2, manga_code
    with col0_1:
        manga_code = st.text_input("Manga's Code:", 'ne990439')
    with col0_2:
        st.markdown("To find a code, search in [Manganelo](https://ww5.manganelo.tv/)")
        if st.checkbox('Search manga'):
            clean_mangas()
            clean_imgs()
            chapters_elements = get_chapters_elements(manga_code)
            select_chapters()

def select_chapters():
    global chapters_names, chapters_elements, col0_1, manga_code, selected_chapters_name
    if len(chapters_elements) != 0:
            chapters_names = [chapter_element.text for chapter_element in chapters_elements]
            chapters_names.reverse()
    with col0_1:
        selected_chapters_name = st.multiselect(
            'Select the chapters you want to download:',
            chapters_names)
        if st.checkbox('Ready...'):
            if len(selected_chapters_name) != 0:
                print('Hola mundo')

find_manga()

# chapters_elements = get_chapters_elements(manga_code)
# selected_chapters_elements = select_chapters_elements(chapters_elements)

