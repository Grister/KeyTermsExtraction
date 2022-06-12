# put your python code here
import nltk
from collections import Counter

text = input().split()

pos_tags = nltk.pos_tag(text)
poses = [pos for (word, pos) in pos_tags]

print(Counter(poses).most_common(1)[0][0])

