import streamlit as st
from utils.st_def import st_logo, st_text_cleaning_contents

st_logo(title = "Welcome 👋 to Text Cleaning!", page_title="Text Cleaning",)
st_text_cleaning_contents()
#------------------------------------------------------------------------
import pandas as pd, re, unicodedata
from bs4 import BeautifulSoup
st.markdown("#### Download Amazon_Unlocked_Mobile.csv from Kaggle.")
df=pd.read_csv('http://hypech.com/data/Amazon_Unlocked_Mobile_Rating_Reviews_1000.csv')
st.write(df.head())
st.write(df['Reviews'].iloc[0])

def remove_html_tags_func(text):        return BeautifulSoup(text, 'html.parser').get_text()
def remove_url_func(text):              return re.sub(r'https?://\S+|www\.\S+', '', text)
def remove_accented_chars_func(text):   return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
def remove_punctuation_func(text):      return re.sub(r'[^a-zA-Z0-9]', ' ', text)
def remove_irr_char_func(text):         return re.sub(r'[^a-zA-Z]', ' ', text)
def remove_extra_whitespaces_func(text):return re.sub(r'^\s*|\s\s*', ' ', text).strip()
def word_count_func(text):              return len(text.split())


def main():
    df['Reviews'] = df['Reviews'].astype(str)   # To be on the safe side, I convert the reviews as strings to be able to work with them correctly.
    df['Clean_Reviews'] = df['Reviews'].str.lower()
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_html_tags_func)
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_url_func)
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_accented_chars_func)
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_punctuation_func)
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_irr_char_func)
    df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_extra_whitespaces_func)
    st.text(df.head())
    df['Word_Count'] = df['Clean_Reviews'].apply(word_count_func)
    st.write(df['Word_Count'])
    st.write(df[['Clean_Reviews', 'Word_Count']].head())
    st.write('Average of words counted: ' + str(df['Word_Count'].mean()))

if st.button("Click button to clean these Reviews", type="primary"):
    main()
