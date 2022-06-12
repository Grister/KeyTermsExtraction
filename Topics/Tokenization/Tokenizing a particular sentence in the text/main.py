from nltk.tokenize import regexp_tokenize, sent_tokenize

string = input()
n = int(input())

sent = sent_tokenize(string)
print(regexp_tokenize(sent[n], r"[A-z']+"))