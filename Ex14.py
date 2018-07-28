import numpy as np
from sys import argv
pi=np.pi
def cir(r):
    return 2*r*pi
script,c=argv
c=float(c)
c1=cir(6317)
c2=cir(3318)
if (c>(0.5*c1+0.5*c2)):
    print "more similar to earth"
elif (c<(0.5*c1+0.5*c2)):
    print "more similar to Mars"
else:
    print "middle of earth and mars"



