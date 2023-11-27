class student:
    counter=0
    def __init__(self,n,m):
        self.name=n
        self.marks=m
        student.counter +=1
    def display(self):
        print(self.name)
        print(self.marks)
    def obj_count(cls):
        print(student.counter)
    
if __name__=='__main__':
    s1=student('pratham',80)
    s2=student('satvik',35)
    s1.display()
    s2.display()
    student.obj_count(student)
