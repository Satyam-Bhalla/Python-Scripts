#Profanity alert
from urllib import request,parse

def read_text():
    quotes = open("W:\Profanity.txt")#Enter the path of text file in "double quotes"
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(text_to_check)
    connection = request.urlopen(url)
    output = connection.read()
    #print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert!!")
    elif b"false" in output:
        print("No curse words")
    else:
        print("There was a problem")

read_text()
