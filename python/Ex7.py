import numpy as np
from sys import argv
script,r=argv
#print"The script is called:",script
#print"r is:",r
r=float(r)
pi=np.pi
l=2*r*pi
s=4*pi*r*r
#print "the circumference of the earth equator is",l,"km"
#print"the cir of the earth equator is %r "%l,"km"
#print"the c of the eartn eqator is %s"%l,"km"
#print"the c of the earth eqtr is %d"%l,"km"
#print"the c of the earth eqtr is %r"%str(l),"km"
print"earth\n\t*circumference of the eqtr is\t",l,"km\n\t*surface is\t",s,"km^2"
print"earth\n\t*c of the etr is \t %s km\n\t*sfc is \t\t %s km^2"%(l,s)
r=raw_input("Please input r: ")
r=float(r)
pi=np.pi
l=2*r*pi
s=4*pi*r*r
#print "the circumference of the earth equator is",l,"km"
#print"the cir of the earth equator is %r "%l,"km"
#print"the c of the eartn eqator is %s"%l,"km"
#print"the c of the earth eqtr is %d"%l,"km"
#print"the c of the earth eqtr is %r"%str(l),"km"
print"earth\n\t*circumference of the eqtr is\t",l,"km\n\t*surface is\t",s,"km^2"
print"earth\n\t*c of the etr is \t %s km\n\t*sfc is \t\t %s km^2"%(l,s)
