from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def _create_dictionary_table(text_string) -> dict:

    # Removing stop words
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    stem = PorterStemmer()  # Reducing words to their root form

    # Creating dictionary for the word frequency table
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1
    return frequency_table

def main():
    with open('https://www.hypech.com/data/storespark.txt') as f:
        article = f.read()
    frequency_table = _create_dictionary_table(article)     # Creating a dictionary for the word frequency table
    print(frequency_table)
    
#     # Tokenizing the sentences
#     sentences = sent_tokenize(article)

#     # Algorithm for scoring a sentence by its words
#     sentence_scores = _calculate_sentence_scores(sentences, frequency_table)

#     # Getting the threshold
#     threshold = _calculate_average_score(sentence_scores)

#     # Producing the summary
#     article_summary = _get_article_summary(sentences, sentence_scores, 1.5 * threshold)

#     print(article_summary)

if __name__ == "__main__":
    main()
