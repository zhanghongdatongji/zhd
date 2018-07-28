from sys import argv
script,rawfile,newfile=argv
text=open(rawfile,'r')
s=text.read()
text1=open(newfile,'a+')
text1.write(s)
text1.seek(0)
text1.close()

