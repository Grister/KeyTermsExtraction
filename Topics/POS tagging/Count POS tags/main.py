# put your python code here
# put your python code here
import nltk
from collections import Counter

text = input()
tagger = nltk.tokenize.word_tokenize(text)

pos_tags = nltk.pos_tag(tagger)
poses = [pos for (word, pos) in pos_tags]

print(dict(Counter(poses)))
