import random

articles = ("the","a","another")
subjects = ("cat","dog","man","woman")
verbs = ("sang","ran","jumped")
adverbs = ("loudly","quietly","well","badly")


cnt = 5
while cnt > 0:
    sentence = ""
    choice = random.randint(0,1)
    if choice == 0:
        sentence = sentence + random.choice(articles) + " "
        sentence = sentence + random.choice(subjects) + " "
        sentence = sentence + random.choice(verbs) + " "
        sentence = sentence + random.choice(adverbs) + " "
    else:
        sentence = sentence + random.choice(articles) + " "
        sentence = sentence + random.choice(subjects) + " "
        sentence = sentence + random.choice(verbs) + " "
    print(sentence)
    cnt -= 1
