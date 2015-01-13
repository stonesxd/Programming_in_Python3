#返回默认值defualt，或者有效值(>= minimum)
def get_int(msg, minimum, default): #msg: 提示信息，minimum：最小值，default：默认值
    while True:
        try:
            line = input(msg)
            if not line and default is not None:    #如果line为空""，是不能进行int()转化的
                return default
            i = int(line)
            if i < minimum:         #检查输入值是否比最小值要小
                print("must be >= ", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


import random

rows = get_int("rows:", 1, None)
cols = get_int("columns:", 1, None)
mini = get_int("minimum (or Enter for 0):", -100000, 0)
default = 1000
if default < mini:
    default = 2 * default
maxi = get_int("minimum (or Enter for " + str(default) + "):", mini, default)

row = 0
while row < rows:
    numline = ""
    col = 0
    while col < cols:
        ele = random.randint(mini, maxi)
        sele = str(ele)
        while len(sele) < 10:   #以10字符长度对齐
            sele = " " + sele
        numline += sele
        col += 1
    print(numline)
    row += 1
        
