for i in range(11):
    
    print i,"*",i,"=",(float(i)/10.0+1)*(float(i)/10.0+1)

a=[]
for i in range(11):
    i=i/10.0+1.0
    a.append(i*i)
print a
