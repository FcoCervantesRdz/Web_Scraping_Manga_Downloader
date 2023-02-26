import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="FAQ", 
    page_icon="❓"
)

st.markdown("""
    # FAQ ❓
    1. How do I use the Manga Downloader?
    2. How do I get the manga's code?
    ----
    ## 01 - How do I use the Manga Downloader?
    In order to use this tool, you will follow the next stepts:
    1. Go to [Maganelo](https://ww5.manganelo.tv/) and search for any manga you like.
    2. Copy the manga's code an paste it on the textbox in the Manga Downloader.
    3. Press 'enter' and choose the chapters you want from the multi selector.
    4. After that, click on the box 'Chapters selected...'
    5. Wait until all the chapters are downloaded.
    6. Download the chapters using que buttons.

    Important notes:
    * If you put an incorrect manga code, the manga downloader will advise you about that
    * If you want to select a big amount of chapters, keep in mind that you will be able to download them after 
      all of them were completed loaded.
    ----
    ## 02 - How do I get the manga's code?
    After you select any manga and you can see it's page (for example: 
    [*Beyond the sky*](https://ww5.manganelo.tv/manga/manga-ne990439)), you will be able 
    to see the code on the url after 'ww5.manganelo.tv/manga/manga-', as you can apreciate in the image:
""")
st.image(Image.open('./../imgs/manga_url_ss.png'), caption='Manga_url SS')
st.markdown("""
    In this example, the code is 'ne990439'
""")
