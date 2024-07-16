A Document Search Engine project with TF-IDF.
# Prerequisites
---
- Python 3.5+
- pip3
- NLTK
- Scikit-learn

# 1. Data Collection
---
Here, we are using a custom dataset with data scraped from [No Starch Press](https://nostarch.com).
The dataset contains a collection of books published by the publication under tag [Programming](https://nostarch.com/catalog/programming).
## 1.1 Data Cleaning: 
---
In this step we clean the scraped data, removing any unnecessary characters.

```python
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
```
## 1.2 Data Pre-processing
---
In this step, the cleaned data is pre-processed before creating the inverted index of tokens.
The pre-processing pipeline includes tokenizing each sentence, removing stop words and finally stemming. 

```python
for name in pub_list_special_rm:  
    words = word_tokenize(name)  
    stem_word = ""  
    for a in words:  
        if a.lower() not in STOPWORDS:  
            stem_word += stemmer.stem(a) + ' '  
    pub_list_stemmed.append(stem_word.lower())
```

# 2.Indexing
---
An Inverted Index is created with each token of all sentences as keys and their indexes as values.

```python
data_dict = {}  
  
for a in range(len(pub_list_stemmed)):  
    for b in pub_list_stemmed[a].split():  
        if b not in data_dict:  
            data_dict[b] = [a]  
        else:  
            data_dict[b].append(a)
```

### Inverted Index 
---
<img src="https://github.com/user-attachments/assets/66d85ef3-3370-4b01-9f37-5ff8241b209e" width=500px>

# 3. Search Engine
---
This Search Engine uses the TF-IDF algorithm.
[**TF-IDF**](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) stands for **“Term Frequency — Inverse Document Frequency”**. This is a technique to calculate the weight of each word signifies the importance of the word in the document and corpus
## 3.1 Calculating ranking using [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity).
---
It is the most common metric used to calculate the similarity between document text.
<img src="https://github.com/user-attachments/assets/36662b88-702d-4e22-872b-5d1560dc7d9b" width=500px>

## Generating TF-IDF using TfidfVectorizer
---
```python
temp_file = tfidf.fit_transform(temp_file)  
cosine_output = cosine_similarity(temp_file, tfidf.transform(stem_word_file))  
```

# Testing the function
---
```python
search_data('python')
```
<img src="https://github.com/user-attachments/assets/060be523-6dcb-40c7-ae88-7e4d07cc0642" width=500px>

**Result of similar documents for word "Python".** 

# Conclusion
---
The search engine at the current stage has very limited capability.
Using a vector encoder model would provide sematic search results that are similar in meaning while TF-IDF model doesn't understand words.

