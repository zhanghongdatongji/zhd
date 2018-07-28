class organism(object):
    def __init__(self):
        super(organism,self).__init__()
        self.carbon=True
        self.oxygen=True
    def rot(self):
        print "It rots"
class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.O2=True   
    def move(self):
        print "It's alive and it moves!!!"
class vertebrate(animal):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.vrtb=True
    def bone(self):
        print "It has bones"
class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.milk=True
        self.egg=False
    def vivi(self):
        print "It procedures viviparism"
class dog(mammal):
    def __init__(self):
        super(dog,self).__init__()
        self.hunt=True
        self.danger=True
    def humane(self):
        print "It can be friendly to humanity!!!"
        
