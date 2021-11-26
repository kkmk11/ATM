#ATM
from datetime import datetime
class ATM:
    def __init__(self):
        self.money=50000  #Initial Bank balance
        self.pin=0000     #Initial PIN 
        self.tr=[]
    def withdraw(self,wd):
        p=int(input("Enter th pin : "))
        if(p==self.pin):
            if(self.money>wd):
                self.money=self.money-wd
                x=datetime.now()
                print("Balance amount is : {0}                Transaction time : {1}\n".format(self.money,x))
                wd= f'{x}      -{wd}'
                self.tr.append(wd)
            else:
                print("Insufficient")
        else:
            print("WRONG PIN")
    def deposit(self,dp):
        p=int(input("Enter th pin : "))
        if(p==self.pin):
            self.money=self.money+dp
            x=datetime.now()
            print("Balance amount is : {0}                Transaction time : {1}\n".format(self.money,x))
            dp= f'{x}      +{dp}'
            self.tr.append(dp)
        else:
            print("WRONG PIN")
    def changepin(self):
        k=int(input("Enter the previous pin : "))
        if(k==self.pin):
            self.pin=int(input("Enter the new pin : "));
            l=int(input("Confirm the PIN : "));
            x=datetime.now()
            if(self.pin==l):
                print("PIN succesfully updated !!           Updated time : {0}\n".format(x))
                j= f'{x}       PIN updated'
                self.tr.append(j)
            else:
                print("Try Again !!")
        else:
            print("WRONG PIN")
    def transaction(self):
        k=int(input("Enter the PIN : "))
        print("Mini Transaction history : ")
        if(k==self.pin):
            if(len(self.tr)!=0):
                print("|-----------------------------------------------------------|")
                for i in range(len(self.tr)):
                    print("|  {0})    {1}              |".format(i+1,self.tr[i]))
                print("|-----------------------------------------------------------|")
                print("Total balance :",self.money)
                print("\n")
            else:
                print("Empty Record\n")
        else:
            print("WRONG PIN")

x=ATM()
for i in range(10):
    c=int(input("1)Withdraw money\n2)Deposit money\n3)Change the pin\n4)Mini Transaction History\n5)Exit\n\nEnter the option you need : "))
    if(c==1):
        wd=int(input("Enter the amount to withdraw : "))
        x.withdraw(wd)
    if(c==2):
        dp=int(input("Enter the amount to deposit : "))
        x.deposit(dp)
    if(c==3):
        x.changepin()
    if(c==4):
        x.transaction()
    if(c==5):
        exit(0)
