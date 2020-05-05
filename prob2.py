from math import pi
import random
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#   CIRCLE CLASS AND METHODS
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
class circle():
    def __init__(self,radius):  
        self.radius = radius
    
    #calculate area    
    def area(self):
        return pi*self.radius**2

#Code TO GET AREA OF A CIRCLE BY PASSING A RADIUS
def calcArea():    
    area1 = circle(5)
    return area1.area()

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#   LIST CLASS AND METHODS
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
class myList():
    def __init__(self,args):
        self.args = args

    def sumList(self):
        return sum(self.args)

    def getMinVal(self):
        return min(self.args) 

# code to get the sum of a list
def getListSum():
    l1 = myList([2,4,6,5,8,9])
    return l1.sumList()

# code to get minimum value of a list
def getMin():
    l1 = myList([2,4,6,5,8,9])
    return l1.getMinVal()

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#   SIMULATING DICE ROLL UNTIL 5 IS OBTAINED
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

def dice():
    roll = random.randint(1,6)
    while roll != 5:
        roll = random.randint(1,6)
    else:
        return roll
