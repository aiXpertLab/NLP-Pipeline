# if 'sentences' not in st.session_state:   st.session_state['sentences'] = ''
from nltk.tokenize import sent_tokenize
import streamlit as st
from utils.st_def import st_logo, st_feature_engineering

st_logo(title = "Welcome 👋 to Feature Engineering!", page_title="Feature Engineering",)
st_feature_engineering()

def sentences():
    if 'article_content' not in st.session_state:
        st.info("Run Data Acquisition first.")
    else:
        txt = st.session_state['article_content']
        sentences = sent_tokenize(txt)      #Step 3:  Tokenizing the article into sentences. To split the article_content into a set of sentences, we’ll use the built-in method from the nltk library.
        if 'sentences' not in st.session_state:   st.session_state['sentences'] = ''
        st.session_state['sentences'] = sentences
        return sentences
        # st.write(f"You entered: {st.session_state['article_content']}")

if __name__ == '__main__':
    sentences = sentences()
    st.write(sentences)
