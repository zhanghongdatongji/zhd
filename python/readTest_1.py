from sys import argv
textfile=raw_input("Please print a txt filename: ")
text=open(textfile)
print"The content of %s:"% textfile
print text.read()

