class Account :
    def createAccount(self):
        
        validAccNo=False
        while not validAccNo:
          accNo= input("Enter the account no : ")
          if len(accNo)==7 and accNo.isdigit():    
            validAccNo=True
          else:
            print("Account Number Must Contain 7 Digits only..")
        print("Account Number : "+ accNo)   
        

        self.name = input("Enter the account holder name : ")

        for char in self.name:
          if not char.isalpha():
            print("Invalid name")
            name = input("Enter the account holder name : ")

        self.type = input("Ente the type of account [Current/Saving] : ")
        self.deposit = float(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")
    
       # print("Account Number : ",accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)

    def depositamount(self): 
        self.balance=self.deposit
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",self.balance) 
  
    def withdraw(self): 
        amount=float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
          self.balance-=amount 
          print("\n You Withdrew:",amount)   
        else: 
           print("\n Insufficient balance  ") 
    
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

obj_s = Account() 
obj_s.createAccount()
obj_s.depositamount() 
obj_s.withdraw() 
obj_s.display() 

      
    
    
    
    
    
    
    
    
    
    
