import numpy
i=0
while i<521:
    print "I love tiantian"
    i+=1
print i

print "the code using while only:"
i=0
m=float(raw_input("please input a num used to judge:  "))
n=numpy.random.randn(1)
while n<m:
    print "the previous rand num is",n,
    n=numpy.random.randn(1)
    print "\tthe current rand num is",n
    i+=1
    #if 1>1000:
    #quit???
print "\ntimes while suring whether it's smaller than ",m," is:",i

