from nltk.tokenize import word_tokenize, sent_tokenize

import streamlit as st, urllib
from utils.utilities import get_products, aichat
from utils.st_def import st_logo, st_case_study

st_logo(title = "Welcome 👋 to Model Buiding!", page_title="Build it up",)
st_case_study()

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import bs4 as BeautifulSoup
import urllib.request  

# Step 4: Finding the weighted frequencies of the sentences
# To evaluate the score for every sentence in the text, we’ll be analyzing the frequency of occurrence of each term. 
# In this case, we’ll be scoring each sentence by its words; that is, adding the frequency of each important word found in the sentence.
def _calculate_sentence_scores(sentences, frequency_table) -> dict:   
    
    #algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]

        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words
  

    return sentence_weight

# Step 5: Calculating the threshold of the sentences
def _calculate_average_score(sentence_weight) -> int:   
   
    #calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    #getting sentence average value from source text
    average_score = (sum_values / len(sentence_weight))

    return average_score

def _get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
            article_summary += " " + sentence
            sentence_counter += 1

    return article_summary

# Step 6: Getting the summary
if __name__ == '__main__':
    if 'article_content' not in st.session_state:
        st.info("Run Data Acquisition first.")
    elif 'frequency_table' not in st.session_state:
        st.info("Run Text Preprocessing please.")
    elif 'sentences' not in st.session_state:
        st.info("Run Feature Engineering please.")
    else:
        frequency_table = st.session_state['frequency_table']   #1 creating a dictionary for the word frequency table
        sentences =  st.session_state['sentences']              #2 tokenizing the sentences
        sentence_scores = _calculate_sentence_scores(sentences, frequency_table)#3 algorithm for scoring a sentence by its words
        threshold = _calculate_average_score(sentence_scores)   #4 getting the threshold
        article_summary = _get_article_summary(sentences, sentence_scores, 1.5 * threshold)#5 producing the summary
        st.header("Article Summary: ")
        st.write(article_summary)