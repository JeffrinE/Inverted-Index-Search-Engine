import os
import json
import ujson
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer()

pub_name = []
pub_url = []
pub_author = []

with open('scraper_results.json', 'r') as f:    doc = f.read()
scraper_result = ujson.loads(doc)

for item in scraper_result:
    pub_name.append(item['name'])
    pub_url.append(item['link'])
    pub_author.append(item['author'])

with open('publication_list_stemmed.json', 'r') as f:   doc = f.read()
pub_list_stemmed = ujson.loads(doc)

with open('publication_indexed_dictionary.json', 'r') as f: doc = f.read()
data_dict = ujson.loads(doc)

#StopWord PreDefinition
STOPWORDS = stopwords.words('english')
stemmer = PorterStemmer()

collective_output = {}


def search_data(inp):
    inp = inp.lower().split()
    output = {}
    pointer = []
    for token in inp:
        stem_temp = ""
        stem_word_file = []
        temp_file = []

        word_list = word_tokenize(token)
        for x in word_list:
            if x not in STOPWORDS:
                stem_temp += stemmer.stem(x) + " "
        stem_word_file.append(stem_temp)

        pointer = data_dict.get(stem_word_file[0].strip())
        if pointer == None:
            output = {}
        else:
            for j in pointer:   temp_file.append(pub_list_stemmed[j])
            temp_file = tfidf.fit_transform(temp_file)
            cosine_output = cosine_similarity(temp_file, tfidf.transform(stem_word_file))
            for j in pointer:   output[j] = cosine_output[pointer.index(j)]

        collective_output.update(output)

    sorting = sorted(collective_output.items(), key=min, reverse=True)
    print(f"SEARCH QUERY: {" ".join(inp)}")
    print(f"{len(collective_output)} searches found.\n")
    for (a, b) in sorting:
        print(f"{pub_name[a]}\n{pub_url[a]}\n{pub_author[a]}\n-------")


search_data("art")
