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


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_field(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",","") #if number is '1,555', then -> 1555
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
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
                
    

def main():
    maxwidth = 100
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
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

main()
