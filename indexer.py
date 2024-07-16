import os
import ujson
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


with open('scraper_results.json', 'r') as f:
    scraper_results = f.read()
data_dict = json.loads(scraper_results)

pub_name = []
pub_url = []
pub_author = []


for item in data_dict:
    pub_name.append(item['name'])
    pub_url.append(item['link'])
    pub_author.append(item['author'])


#StopWord PreDefinition
STOPWORDS = stopwords.words('english')
stemmer = PorterStemmer()


pub_list = []
pub_list_special_rm = []
pub_list_stemmed =[]

#Remove all Special Chars
special_chars = '''!()--[]{};:'"\\, <>./?@#$%^&*_~0123456789+='''''

for file in pub_name:
    word_sc_rm = ""
    if len(file.split()) ==1 :
        pub_list_special_rm.append(file)
    else:
        for a in file:
            if a in special_chars:
                word_sc_rm += ' '
            else:
                word_sc_rm += a
        pub_list_special_rm.append(word_sc_rm)


for name in pub_list_special_rm:
    words = word_tokenize(name)
    stem_word = ""
    for a in words:
        if a.lower() not in STOPWORDS:
            stem_word += stemmer.stem(a) + ' '
    pub_list_stemmed.append(stem_word.lower())

data_dict = {}

for a in range(len(pub_list_stemmed)):
    for b in pub_list_stemmed[a].split():
        if b not in data_dict:
            data_dict[b] = [a]
        else:
            data_dict[b].append(a)

with open('publication_list_stemmed.json', 'w') as f:
    json_str = ujson.dumps(pub_list_stemmed)
    f.write(json_str)


with open('publication_indexed_dictionary.json', 'w') as f:
    print(data_dict)
    json_str = ujson.dumps(data_dict)
    f.write(json_str)

