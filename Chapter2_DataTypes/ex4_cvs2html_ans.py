#Delete the escape_html() function from csv2html.py, and use the xml.sax.
#saxutils.escape() function from the xml.sax.saxutils module instead.

import sys
import xml.sax.saxutils

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def extract_field(line):                #input a string
    fields = []
    field = ""
    quote = None
    for c in line:  # line is string, c means char
        if c in "\"'":  # deals with quoted string
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ',':  #end of a field
            fields.append(field)
            field = ""
        else:
            field += c                  #accumulating a field
    if field:
        fields.append(field)            #adding the last field
    return fields                       #return a list

#replace spceial HTML character with the appropriate HTML entity
#def escape_html(text):
#    text = text.replace("&", "&amp;")   #must replace first
#    text = text.replace("<", "&lt;")
#    text = text.replace(">", "&gt;")
#    return text


def print_line(line, color, maxwidth, formatstr):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_field(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",","") #if number is '1,555', then -> 1555
            try:
                x = float(number)
                print(("<td align='right'>{0:"+formatstr+"}</td>").format(round(x)))
            except ValueError:
                field = field.title()   #string deal, str.title() 
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:  #fixed the field length
                    field = xml.sax.saxutils.escape(field)
                else:
#                    field = "{0} ...".format(escape_html(field[:maxwidth]))
                    field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")

# This function should be called from main() and should
#return a tuple of two values: maxwidth (an int) and format (a str). When
#process_options() is called it should set a default maxwidth of 100, and a
#default format of “.0f”—this will be used as the format speciﬁer when out-
#putting numbers.
def process_option():
    maxwidth = 100
    formatstr = ".0f"
    if len(sys.argv) > 1:
        if sys.argv[1] in {"-h","--help"}:
            helptext = '''usage:

csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html
maxwidth is an optional integer; if specified, it sets the maximum
number of characters that can be output for string fields,
otherwise a default of 100 characters is used.

format is the format to use for numbers; if not specified it
defaults to ".0f".'''
            print(helptext)
            return (None,None)
        else:
            try:
                num = sys.argv[1].find('=') + 1
                maxwidth = int(sys.argv[1][num:])
            except TypeError as err:
                print(err)
                print(helptext)
        if len(sys.argv) == 3:
            num = sys.argv[2].find('=') + 1      
            formatstr = sys.argv[2][num:]
        else:
            print(helptext)
    return (maxwidth,formatstr)
            
            
def main():
    (maxwidth, formatstr) = process_option()
    if maxwidth == None:
        return
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = 'lightgreen'
            elif count % 2:
                color = 'white'
            else:
                color = 'lightyellow'
            print_line(line, color, maxwidth, formatstr)
            count += 1
        except EOFError:
            break
    print_end()

# usage: csv2html2_ans.py maxwidth=20 format=0.2f < mydata.csv > mydata.html
main()
