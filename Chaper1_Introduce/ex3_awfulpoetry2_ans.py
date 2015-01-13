import random
import sys

articles = ("the","a","another")
subjects = ("cat","dog","man","woman")
verbs = ("sang","ran","jumped")
adverbs = ("loudly","quietly","well","badly")

cnt = 5
# 方法一
if len(sys.argv) > 1:   
    try:
        cnt = int(sys.argv[1])
    except ValueError as err:
        print(err)
# 方法二
#try:
#    cnt = int(sys.argv[1])
#except ValueError as err:
#    print(err)
#except IndexError as err:
#    pass
    

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
