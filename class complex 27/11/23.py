class Complex:
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary
    def display(self):
        print(self.real,"+",self.imaginary,"i")
    def add(self,c1,c2):
        self.real=c1.real+c2.real
        self.imaginary=c1.imaginary+c2.imaginary
        
if __name__=='__main__':
    c1=Complex(10,3)
    c2=Complex(9,4)
    c1.display()
    c2.display()
    c3=Complex()
    c3.add(c1,c2)
    c3.display()
