# @ windowns platform

import sys
import unicodedata

def print_unicode_table(words):
    filename = "unicode-table.txt"
    fh = open(filename, "w", encoding="utf8")
    fh.write("decial  hex  chr {0:^40}\n".format("name"))
    fh.write("------ ----- --- {0:-<40}\n".format(""))

    code = ord(" ")
    end = min(0xD800,sys.maxunicode)    #stop at surrogate pairs
    
    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknow ***")
        # judge every word in name?
        cnt = 0
        inflag = True
        while cnt < len(words):
            inflag &= words[cnt] is None or words[cnt] in name.lower()
            cnt += 1
        if inflag:
            fh.write("{0:6} {0:5X} {0:^3c} {1}\n".format(code,name.title()))
        code += 1
    print("write result to:", filename)
    fh.close()

words = [None]  #use words list for several seperate words
if len(sys.argv) > 1:
    if sys.argv[1] in {'-h','--help'}:
        print("usage: {0} [string] [string]".format(sys.argv[0]))
        word = 0
    else:
        words = sys.argv[1:]
if words != 0:
    print_unicode_table(words)
