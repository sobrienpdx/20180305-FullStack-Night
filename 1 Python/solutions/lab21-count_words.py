# lab 21 - count_words.py

import os, string

def count_words(words, counter=None):
	"""
	returns counter (dict) of normalized words
	"""
	if not counter:
		counter = {}
	words = words.translate(str.maketrans({word:None for word in string.punctuation})).lower().split()
	for word in words:
		if word in counter.keys():
			counter[word] += 1
		else:
			counter[word] = 1
	return counter

def remove_stopwords(counter):
	"""
	removes common english words
	"""
	stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
	for word in stopwords: # remove word from counter if in stopwords
		if word in counter.keys():
			counter.pop(word)
	return counter


if __name__ == '__main__':
	book_dir = os.path.join(os.getcwd(), 'count_words')
	for file in os.listdir(book_dir):
		if file.endswith('.txt'):
			with open(os.path.join(book_dir, file)) as book:
				text = book.read()
				word_count = remove_stopwords(count_words(text))
				words = list(word_count.items()) # .items() returns a list of tuples
				words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
				for i in range(min(20, len(words))):  # print the top 20 words, or all of them, whichever is smaller
				    print(words[i])				