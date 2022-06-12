import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

poses = dict(nltk.pos_tag(sent))

print(poses['raced'])
