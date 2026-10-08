class BankAccount:
    def __init__(self, account number, balance): # Make account
        self.__account_number = account number # Make private accounter number
        self.__balance = balance # This is your private balance
        
    def set_account_number(self, account_number): # this is a setter for account number
        self.__account_number = account_number
        
    def set_balance(self, balance): #this is also a setter but for balance
        if balance >= 0: #this is to check that the balance isn't negative
            self.__balance = balance
        else:
            print("Hey! The balance must NOT be a negative value.") #this is to give the user a warning in the case that their balance is negATIVE

    @property
    def account_number(self): #this is the getter for account number added also the property decorator
        return self.__account_number
    
    @property
    def balance(self): #getter for balance w/ decorator
        return self.__balance
    
a1 = BankAccount(12345, 1000) #will create an object for bankaccount

print("Account 1")
print(f"Account Number: {a1.account_number}") #this shows the account number to the user
print(f"Balance: {a1.balance:.2f}") #shows balance
print()
print("Update balance to -100") #ttesting the waters
a1.set_balance(-100) 
print(f"Account Number: {a1.account_number}") # displays acc number
print(f"Balance: {a1.balance:.2f}") #displays the balance (which is unchanged)dx  
