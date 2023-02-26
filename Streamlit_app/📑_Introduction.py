import streamlit as st
from PIL import Image
from functions import clean_mangas
clean_mangas()
st.set_page_config(
    page_title="Introduction", 
    page_icon="👋"
)

st.markdown("""
    # Manga Downloader with Web Scrapping!
    There are free options to read manga online, but in some of them, we aren't able to download a PDF version of it to read it later. This is the case of manganelo.tv (https://ww5.manganelo.tv/), where we can just read manga in the page from images loading in the web page.

    These are links examples for diferent mangas:
    * "*Beyond The Sky*": https://ww5.manganelo.tv/manga/manga-ne990439.
    * "*My Wife Is A Fox Spirit*": https://ww5.manganelo.tv/manga/manga-hr984452.
    * "*Fight Class 3*": https://ww5.manganelo.tv/manga/manga-cd980038.

    In this URL structure, we are able to notice that "*ne990439*", "*hr984452*" & "*cd980038*" represents the manga's unique codes.

    Inside every manga's page, we have acces to the list of chapters and their information, as we can see in the next screeshot from the "Beyond The Sky"'s page:
""")
st.image(Image.open('./../imgs/manga_ss.PNG'), caption='Manga SS')
st.markdown("""

    And, inside a chapter's page we can see the images:
""")
st.image(Image.open('./../imgs/chapter_ss.PNG'), caption='Chapter SS')
st.markdown("""

    ## 02 - Objective
    * Build a program to download an specific number of chapters for an asked manga.
    * The program will asks for the unique code that appears in the url's manga.
    * It has to shows the list of chapters to ask for the searched chapters.
    * For the UI, we will work on streamlit app
      
    ## 03 - Result
    You can access to the downloader by clicking 'Manga Downloader' on the left 👈, please 
    feel free to download any manga.

    For feedback and recomendations, I let you my info:
    * 🟦 *LinkedIn*: [@FcoCervantesRdz](https://www.linkedin.com/in/fcocervantesrdz/)
    * 📧 *Mail*: [fco.cervantesrdz@gmail.com](mailto:fco.cervantesrdz@gmail.com)
""")



