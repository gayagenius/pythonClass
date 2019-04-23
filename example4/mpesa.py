

class Mpesa_Account:

	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance

	def deposit(self,amount):
		self.balance = self.balance + amount
		print ("Dear {}, You have sucessfuly deposited Ksh{} to the phone_number {}.Your new balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))

	def withdraw(self,amount):
		self.balance=self.balance-amount
		print("Dear {},You have withdrawn Kshs{} from the number {} Your new balance is Kshs{}.".format(self.name,amount,self.phone_number,self.balance))


	def check_balance(self):
		print("Dear Customer,Your Mpesa Balance is Kshs{}.".format(self.balance))