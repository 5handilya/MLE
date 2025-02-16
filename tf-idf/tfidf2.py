import math
from collections import defaultdict

stopwords = { "the", "and", "is", "a", "of"}

# Preprocessing
def preprocess(text):
	text = text.lower()
	tokens = text.split()
	return [token for token in tokens if token not in stopwords] # can this be made faster with hashing?

# TFIDF computation
def tf_idf(docs):
	# proprocess all docs
	prepd_docs = [preprocess(doc) for doc in docs]

	n_docs = len(documents)
	word_doc_count = defaultdict(int)
	# calculating unique word frequencies in docs
	for doc in prepd_docs:
		unique_words = set(doc)
		for word in unique_words:
			word_doc_count[word] += 1	

	idf = {word: math.log(n_docs / (count + 1)) for word, count in word_doc_count.items()}

	# computing tfidf
	results = []
	for doc in prepd_docs:
		n_words = len(doc)
		tf = defaultdict(float)
		for word in doc:
			tf[word] += 1 / n_words 
		# main equation
		tfidf = {word: tf[word] * idf[word] for word in tf}
		results.append(tfidf)
	return results

documents = [
	"sometimes i wish i were a lesbian said chandler",
	"need me a large tub of chocolate ice cream",
	"good day for a nice walk with a nice cat",
	"i need to buy 200 roses for valentine's day",
	"the cat sat on the mat",
	"kanye west is over party"
]

print(tf_idf(documents))
	

# nede a much larger dataset, learn IDF from large datasets and apply weighted static:currentset IDF w alpha*() + (1-alpha)*()
