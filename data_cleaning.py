import pandas as pd, re, unicodedata
from bs4 import BeautifulSoup

def min_dataset():
    df = pd.read_csv('Amazon_Unlocked_Mobile.csv')
    print(df.head())

    df = df[['Rating', 'Reviews']][:1000]
    df.to_csv('Amazon_Unlocked_Mobile_Rating_Reviews_1000.csv', index=False)
    
df=pd.read_csv('http://hypech.com/data/Amazon_Unlocked_Mobile_Rating_Reviews_1000.csv')
print(df['Reviews'].iloc[0])
print(df.dtypes)

df['Reviews'] = df['Reviews'].astype(str)   # To be on the safe side, I convert the reviews as strings to be able to work with them correctly.

def remove_html_tags_func(text):        return BeautifulSoup(text, 'html.parser').get_text()
def remove_url_func(text):              return re.sub(r'https?://\S+|www\.\S+', '', text)
def remove_accented_chars_func(text):   return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
def remove_punctuation_func(text):      return re.sub(r'[^a-zA-Z0-9]', ' ', text)
def remove_irr_char_func(text):         return re.sub(r'[^a-zA-Z]', ' ', text)
def remove_extra_whitespaces_func(text):return re.sub(r'^\s*|\s\s*', ' ', text).strip()
def word_count_func(text):              return len(text.split())

print(df.head())
df['Clean_Reviews'] = df['Reviews'].str.lower()
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_html_tags_func)
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_url_func)
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_accented_chars_func)
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_punctuation_func)
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_irr_char_func)
df['Clean_Reviews'] = df['Clean_Reviews'].apply(remove_extra_whitespaces_func)
print(df.head())

print(df['Reviews'].iloc[0])
print(df['Clean_Reviews'].iloc[0])

df['Word_Count'] = df['Clean_Reviews'].apply(word_count_func)
print(df[['Clean_Reviews', 'Word_Count']].head())
print('Average of words counted: ' + str(df['Word_Count'].mean()))
df.to_csv('Amazon_Unlocked_Mobile_Rating_Reviews_1000_cleaned.csv', index=False)
