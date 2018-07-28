from sys import argv
script,textfile=argv
text=open(textfile,'w')
line1="My name is tiantian."
line2="I am 3"
line3="I love zhangxiaobao."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
