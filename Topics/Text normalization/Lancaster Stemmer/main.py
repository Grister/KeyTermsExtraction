from nltk.stem import LancasterStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

# write your code here
stemmer = LancasterStemmer()
for i in sent:
    print(stemmer.stem(i))
