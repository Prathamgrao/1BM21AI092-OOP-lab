class creditcard:
    def __init__(self,acc,limit,balance):
        self.acc=acc
        self.__limit=limit
        self.__balance=balance
    def get_balance(self):
        print("balance is",self.__balance)
    def withdraw(self,amt):
        if amt>self.__limit:
            print("limit exceeded")
        if amt>self.__balance:
            print("balance exceeded")
        else:
            self.__balance-=amt
            print("withdrawn")
    def deposit(self,amt):
        self.__balance+=amt
        print("deposited")
c1=creditcard("palli",2600,560)
c1.get_balance()
c1.withdraw(100)
c1.deposit(1000)
