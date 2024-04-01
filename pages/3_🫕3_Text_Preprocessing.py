# st.session_state['frequency_table'] = frequency_table
import streamlit as st
from utils.st_def import st_logo, st_text_cleaning_contents

st_logo(title = "Welcome 👋 to Text Cleaning!", page_title="Text Cleaning",)
st_text_cleaning_contents()

#------------------------------------------------------------------------
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk import download

download("stopwords")

def _create_dictionary_table(text_string) -> dict:
    stop_words = set(stopwords.words("english"))    # Removing stop words
    words = word_tokenize(text_string)              # tokennize
    stem = PorterStemmer()                          # Reducing words to their root form

    frequency_table = dict()                        # Creating dictionary for the word frequency table
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:    continue
        if wd in frequency_table:            frequency_table[wd] += 1
        else:            frequency_table[wd] = 1
    return frequency_table

def main():
    if 'article_content' not in st.session_state:
        st.info("Run Data Acquisition first.")
    else:
        st.write(f"You entered: {st.session_state['article_content']}")
        txt_string = st.session_state['article_content']
        with st.spinner("data loading..."):
            # txt_string = txt_obj.getvalue().decode("utf-8")
            frequency_table = _create_dictionary_table(text_string=txt_string)     # Creating a dictionary for the word frequency table
        
        st.write("data loaded")            
        if 'article_content' not in st.session_state:   st.session_state['article_content'] = ''
        st.session_state['frequency_table'] = frequency_table
        st.table(frequency_table)

if __name__ == "__main__":
    main()
