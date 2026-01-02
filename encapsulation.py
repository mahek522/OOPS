class AccountHolder:
    def __init__(self):
        self.__balance = 10000  #Private attribute
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >=0:
            self.__balance = amount
        else:
            print("Invalid amount")
account_holder = AccountHolder()
print(account_holder.get_balance())  #Accessing balance via getter
account_holder.set_balance(15000)  #Updating balance via setter
print(account_holder.get_balance()) #Accessing updated balance via getter
# Attempting to access private attribute directly will raise an AttributeError
# print(account_holder.__balance)
print(account_holder.__dict__)  #Shows that __balance is name-mangled