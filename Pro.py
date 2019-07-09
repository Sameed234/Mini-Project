class Bank_Account: 

		# created an function having constructor and default balance is initialized as zero.
    def demo(self): 
        self.balance=0
        print("Hello!!! Welcome to MY Bank") 

    # created an function where we will enter an float amount to be deposited.
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance = amount 
        print("\n Amount Deposited:",amount) 
  
    # created and function withdraw where we will check if balence is greater than amount than it will show
    # amount to be withdrawn or insufficient balance.
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Enter Valid amount  ") 
    # created and function where we will display available balance
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

obj_s = Bank_Account() 
obj_s.deposit() 
obj_s.withdraw() 
obj_s.display() 

