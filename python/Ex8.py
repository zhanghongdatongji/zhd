import numpy as np
pi=np.pi
def cir(r):
    return 2*r*pi 
def sur(r):
    return 4*pi*r*r
r=raw_input("Please input r: ")
r=float(r)
#print "the circumference of the earth equator is",l,"km"
#print"the cir of the earth equator is %r "%l,"km"
#print"the c of the eartn eqator is %s"%l,"km"
#print"the c of the earth eqtr is %d"%l,"km"
#print"the c of the earth eqtr is %r"%str(l),"km"
print"earth\n\t*circumference of the eqtr is\t",cir(r),"km\n\t*surface is\t",sur(r),"km^2"
print"earth\n\t*c of the etr is \t %s km\n\t*sfc is \t\t %s km^2"%(cir(r),sur(r))
r=3378
print"Mars\n\t*circumference of the eqtr is\t",cir(r),"km\n\t*surface is\t",sur(r),"km^2"
print"Mars\n\t*c of the etr is \t %s km\n\t*sfc is \t\t %s km^2"%(cir(r),sur(r))

