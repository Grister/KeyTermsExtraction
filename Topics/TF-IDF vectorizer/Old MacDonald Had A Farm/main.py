#  write your code here 
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1),
                             stop_words=None)

dataset = open('data/dataset/input.txt', 'r')
weighted_matrix = vectorizer.fit_transform([dataset])

print(weighted_matrix[(0, 10)])
