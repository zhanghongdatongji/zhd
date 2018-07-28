#implicit
class parent(object):
    def implicit(self):
        print"parent implicit()"
class child(parent):
    def __init__(self):
        super(child,self).__init__()
dad=parent()
son=child()
dad.implicit()
son.implicit()
#Explicitly override
class parent1(object):
    def override(self):
        print "parent override()"
class child1(parent1):
    def override(self):
        print "child override()"
dad=parent1()
son=child1()
dad.override()
son.override()
#Alter between the two version
class parent2(object):
    def altered(self):
        print "parent altered()"
class child2(parent2):
    def altered(self):
        print "child altered()"
        super(child2,self).altered()
dad=parent2()
son=child2()
dad.altered()
son.altered()
#Mutiple inheritance
class male(object):
    def sp(self):
        print"Man is strong"
class boy(child1,male):
    pass
tony=boy()
tony.sp()
tony.override()
