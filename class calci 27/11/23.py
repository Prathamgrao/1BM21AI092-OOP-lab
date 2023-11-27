class calculator:
    def __init__(self,version):
        self.version=version
    def display(self):
        print(self.version)
    def add(self,n1,n2):
        print(n1+n2)

if __name__=='__main__':
    c1=calculator('casio')
    c2=calculator('lampard')
    c1.display()
    c1.add(30,25)
    c2.display()
    c2.add(30,39)   
