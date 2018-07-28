import numpy as np
from sys import argv
pi=np.pi
def cir(r):
    return 2*r*pi
script,r=argv
#print"The script is called:",script
#print"r is:",r
r=float(r)
#print "the circumference of the earth equator is",l,"km"
#print"the cir of the earth equator is %r "%l,"km"
#print"the c of the eartn eqator is %s"%l,"km"
#print"the c of the earth eqtr is %d"%l,"km"
#print"the c of the earth eqtr is %r"%str(l),"km"
c1=cir(6317)
c2=cir(3318)
if (cir(r)>(0.5*c1+0.5*c2)):
    print "more similar to earth"
elif (cir(r)<(0.5*c1+0.5*c2)):
    print "more similar to Mars"
else:
    print "middle of earth and mars"
    


