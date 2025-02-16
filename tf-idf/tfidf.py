import math
from collections import defaultdict

stopwords = {"the", "and", "is", "a", "of"}

# Turn text to lowercase, split, eliminate stopwords, return
def preprocess(text):
    text = text.lower()
    tokens = text.split()
    return [token for token in tokens if token not in stopwords]

# Main function
def tf_idf(documents):
    # Preprocess all docs
    preprocessed = [preprocess(doc) for doc in documents]
    
    # Compute IDF
    doc_count = len(documents)
    word_doc_count = defaultdict(int)
    # Calculating unique word frequencies in docs
    for doc in preprocessed:
        unique_words = set(doc)
        for word in unique_words:
            word_doc_count[word] += 1
    
    idf = {word: math.log(doc_count / (count + 1)) for word, count in word_doc_count.items()}
    
    # Compute TF-IDF for each document
    tfidf_results = []
    for doc in preprocessed:
        total_words = len(doc)
        tf = defaultdict(float)
        for word in doc:
            tf[word] += 1 / total_words
        tfidf = {word: tf[word] * idf[word] for word in tf}
        tfidf_results.append(tfidf)
    
    return tfidf_results

# Test data 
documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals"
]

print(tf_idf(documents))
