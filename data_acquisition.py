# Data Acquisition

import bs4 as BeautifulSoup
import urllib.request  

fetched_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/20th_century')

article_read = fetched_data.read()

# Parsing the URL content and storing in a variable
article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')

# Returning <p> tags
paragraphs = article_parsed.find_all('p')

article_content = ''
# Looping through the paragraphs and adding them to the variable
for p in paragraphs:  
    article_content += p.text

print(article_content)

with open('data/wiki_20th.txt', "w") as file:
    file.write(article_content)
