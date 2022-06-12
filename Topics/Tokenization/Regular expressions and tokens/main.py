from nltk.tokenize import regexp_tokenize

string = input()

print(regexp_tokenize(string, r"[A-z'-]+"))
