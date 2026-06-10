class Fraction:
    #using constructor 
    def __init__(self,x,y):
        self.num = x
        self.den = y
    
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    #defining Addition 
    def __add__(self,other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    #defining subtraction 
    def __sub__(self,other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    #defining multiply 
    def __mul__(self,other):
        new_num = self.num*other.den * other.num*self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num,new_den)
    #defining division 
    def __div__(self,other):
        new_num = self.num*other.den / other.num*self.den
        new_den = self.den * other.den

        return '{}/{}'.format(new_num,new_den)
    #convert decimal
    def con_to_deci(self):
        return self.num/self.den
    
#defining Variable
fr1 = Fraction(3,5)
fr2 = Fraction(2,5)
print(fr1.con_to_deci())