Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "   * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = [" ****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digit = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

row = 0
try:
    digits = input('Please input a interger:')
    while row < 7: #每个字符为7行字模数据所组成
        line = ''
        col = 0
        #以整行为单位进行链接，打印输出
        while col < len(digits):
            num = int(digits[col])  #每次取一位digits
            digit = Digit[num]      #取当前位数字的字模数据
            #替换字模数据中的*号
            count = 0
            rowstr = ""
            while count < len(digit[row]):
                if digit[row][count] == '*':
                    rowstr += str(num)
                else:
                    rowstr += " "
                count += 1
            line += rowstr + "   "  #以行为单位，链接字模数据
            col += 1
        print(line)
        row += 1
#以防止didits出现异常值
except ValueError as err:
    print(err, "in", digits)
