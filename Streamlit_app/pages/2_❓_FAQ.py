import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="FAQ", 
    page_icon="❓"
)

st.markdown("""
    # FAQ ❓
    1. How do I use the Manga Downloader?
    ----
    ## 01 - How do I use the Manga Downloader?
    In order to use this tool, you will follow the next stepts:
    1. Go to Manga Downloader, this section is available on the left box.
    2. Search for the manga you want on the text box.
    3. Keep in mind that, if Manganelo doesn't have that manga, it will not appear.
    4. Afther that, choose between the results of your search in the select section.
    3. Press 'enter' and choose the chapters you want from the multi selector.
    4. When you ar ready, click on the box 'Chapters selected...'
    5. Wait up to the bars indicate that the conversion to PDF is finished.
    6. Download the chapters using que buttons.

    Important notes:
    * If there aren't results of you search, the manga downloader will advise you about that
    * If you want to select a big amount of chapters, keep in mind that you will be able to download them after 
      all of them were coverted to PDF completly.
    ----
""")