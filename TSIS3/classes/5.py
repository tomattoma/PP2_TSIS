class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposits(self,money):
        self.balance+=money 
        print(f"Money talks! You have {self.balance} money in your account")
    def withdrawals(self,money):
        if self.balance > money:
            print(f"{money} money withdrawn, account balance {self.balance-money}")
        else:
            print("Insufficient funds to withdraw from the account")


Someone = Bank_account(1000,60000)
Someone.deposits(300)