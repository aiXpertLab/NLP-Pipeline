#   st.session_state['article_content'] = article_content

import streamlit as st
from utils.utilities import get_products, aichat
from utils.st_def import st_logo, st_data_acquisition_contents

st_logo("Welcome 👋 to Data Acquisition!", "Data Acquisition")
st_data_acquisition_contents()

placeholder_text = "https://en.wikipedia.org/wiki/20th_century"  # Your placeholder text
url = st.text_input('🌐 Enter your URL: ', placeholder=placeholder_text)

#-----------------------------------------------
import bs4 as BeautifulSoup, time
import urllib.request  

if url:
    try:
        fetched_data = urllib.request.urlopen(url)
        article_read = fetched_data.read()

        article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')    # Parsing the URL content and storing in a variable
        paragraphs = article_parsed.find_all('p')   ## Returning <p> tags
        article_content = ''
        for p in paragraphs:  
            article_content += p.text
            
        if 'article_content' not in st.session_state:   st.session_state['article_content'] = ''
        st.session_state['article_content'] = article_content
        # st.write(f"You entered: {st.session_state['article_content']}")

        def response_generator():
            for word in article_content.split():
                yield word + " "
                time.sleep(0.005)
        st.markdown("### 🔃 we are fetching:")
        st.write_stream(response_generator())
    except Exception as e:
        st.write("Please provide a valid url: ",e.__str__)