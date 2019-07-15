class Account :
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [Current/Saving] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")
    
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)

    def depositamount(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance = amount 
        print("\n Amount Deposited:",amount) 

    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
    # created and function where we will display available balance
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

obj_s = Account() 
obj_s.createAccount()
obj_s.depositamount() 
obj_s.withdraw() 
obj_s.display() 

    	
    
    
    
    
    
    
    
    
    
    
