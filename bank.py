class bank:
    def __init__(self,accno,name,accty,bal):
     self.accno=accno
     self.name=name
     self.accty=accty
     self.bal=0
    def showamt(self):
      print("Account holder name:",self.name)
      print("Account number:",self.accno)
      print("Account type.",self.accty)
      print("Youraccount balace amount.",self.bal)
    def depo(self,d1):
     self.bal=self.bal+d1
     return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("Enter your name:")
a=int(input("Enter your account number:"))
t=input("Enter your account type:")
o=bank(a, n, t, bal=0)
o.showamt()
while (True):
     print("\nMenu")
     print("\n1.Deposit")
     print("\n2.Withdraw")
     c = int(input("Enter your choice:"))
     if (c == 1):
         d = int(input("Enter the amount to deposit"))
         print("Your total balance is", o.depo(d))
     elif(c==2):
         w = int(input("Enter the amount to be withdrawn:"))
         if (w > o.bal):
             print("INSUFFICIENT BALANCE")
         else:
             print("Your total balance Amount is", o.withd(w))
     else:
         print("Enter a valid choice.")
