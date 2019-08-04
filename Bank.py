class Bank:
	def show_bank_details(self):
		
		mylist = []
		accNo = input("Enter the account no : ")
		if len(accNo)==7 and accNo.isdigit():
			
			for i in accNo:
				mylist.append(i)
				#print("Account Number : " + accNo)
		else:
			print("Accout Number must contain at least 7 digits:")
			return(exit())

		

		self.name = input("Enter the account holder name : ")	
		for char in self.name:
			if not char.isalpha():
				print("Invalid name")
				


		self.type = input("Enter the type of account [Current/Saving] : ")
		self.deposit = float(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
		print("\n\n\nAccount Created")

		
		print("Account Holder Name : ", self.name)
		print("Type of Account", self.type)
		print("Balance : ", self.deposit)
		
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
		




if __name__ == '__main__':
        	obj = Bank()
        	obj.show_bank_details()
        	obj.depositamount()
        	obj.withdraw()
        	obj.display()
 

      
    
    
    
    
    
    
    
    
    
    
