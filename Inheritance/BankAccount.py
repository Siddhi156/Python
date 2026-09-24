class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def display(self):
        print("Account Holder: ", self.name)
        print("Account Balance: ", self.balance)

class SavingsAccount(BankAccount):
    def interest(self, rate):
        print("Interest is earned")

account1 = SavingsAccount("Siddhi", 10000)
account2 = SavingsAccount("Samruddhi", 15000) 
account1.display() 
account1.interest(0.05) 
account2.display() 
account2.interest(0.05) 