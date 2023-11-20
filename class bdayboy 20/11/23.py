class birthdayboy():
    name=""
    age=""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Age(self):
        self.age+=1
boy=birthdayboy("pratham",20)
print("the name of birthday boy is",boy.name)
boy.Age()
print(boy.age)
