class BankAccount:    
    def __init__ (self,accnum,accholdername,initialbal):
        self.__accnum=accnum
        self.__accholdername=accholdername
        self.__accbal=initialbal
    def deposit(self,amt):
        if amt>0:
            self.__accbal+=amt
            print(f"DEPOSITED ${amt}.NEW BALANCE:${self.__accbal}")
        else:
            print("INVALID DEPOSIT AMOUNT.AMOUNT MUST BE GREATER THAN 0.")
    def withdraw(self,amt):
        if amt>0 and amt<=self.__accbal:
            self.__accbal-=amt
            print(f"WITHDRAW${amt}.NEWBALANCE:${self.__accbal}")
        elif amt<=0:
            print("INVALID WITHDRAWAL AMOUNT.AMOUNT MUST BE GREATER THAN 0")
        else:
            print("INSUFFICIENT FUNDS FOR WITHDRAWAL.")
    def display(self):
        print("ACCOUNT DETAILS")
        print("***************")
        print(f"ACCOUNT HOLDER:{self.__accholdername}")
        print(f"ACCOUNT NUMBER:{self.__accnum}")
        print(f"ACCOUNT BALANCE:${self.__accbal}")
            
acc=BankAccount("12345","JOHN DOE",1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.display()
        