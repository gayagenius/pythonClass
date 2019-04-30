from datetime import datetime

class Mpesa_Account:

    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.outstanding=[]
        self.repayloan=[]

    def deposit(self,amount):
        now=datetime.now()
        object={"time":now,"amount":amount}
        self.deposits.append(object)
        self.balance = self.balance + amount
        print ("Dear {}, You have sucessfuly deposited Ksh{} to the phone_number {}.Your new balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))

    def withdraw(self,amount):
        if amount < self.balance:
            now=datetime.now()
            object={"time":now,"amount":amount}
            self.withdrawals.append(object) 
            self.balance=self.balance-amount
            print("Dear {},You have withdrawn kshs{} from the number {} Your new balance is kshs{}.".format(self.name,amount,self.phone_number,self.balance))
        else:
             print("Failed.You do not have enough money in your account to withdraw Kshs{}.".format(amount))
    
    def check_balance(self):
        print("Dear Customer,Your Mpesa Balance is Kshs{}.".format(self.balance))

    def my_deposits(self):
        for y in self.deposits:
            time=y["time"]
            formated=time.strftime("%A %d %B %Y")
            amount=y["amount"]
            print("On {} you deposited {}".format(formated,amount))
    def my_withdrawals(self):
        for y in self.withdrawals:
            time=y["time"]
            formated=time.strftime("%A %d %B %Y")
            amount=y["amount"]
            print("On {} you withdrew {}".format(formated,amount))
            
    def give_loan(self,amount):
        total=0
        for x in self.deposits:
            amounts=x["amount"]
            total+=amounts
        if len(self.deposits)>=5 and self.loan==0 and amount<=(total/3):
            now=datetime.now()
            object={"time":now,"amount":amount}
            self.outstanding.append(object)
            self.loan=self.loan+amount
            # self.balance=self.balance+amount
            print("You are able to access our loan services and get a loan of Kshs{},your new balance is Kshs{}".format(self.loan,self.balance))
        else:
            print("You don't have enough credit scores")

    def repay_loan(self,amount):
        if self.loan==0:
            print("You dont have an outstanding loan balance")  
        elif amount<self.loan:
            now=datetime.now()
            object={"time":now,"amount":amount}
            self.repayloan.append(object)
            self.balance=self.balance-amount
            self.loan=self.loan-amount
            print("You have reduced your loan balance by Kshs{}.Your new outstanding loan is Kshs{}.".format(amount,self.loan))
        elif amount==self.loan:
            now=datetime.now()
            object={"time":now,"amount":amount}
            self.repayloan.append(object)
            self.balance=self.balance-amount
            self.loan=self.loan-amount
            print("Congratulations; You have cleared your outstanding loan.")
        elif amount > self.loan:
            now=datetime.now()
            object={"time":now,"amount":amount}
            self.repayloan.append(object)
            rem=amount-self.loan
            self.balance=self.balance-amount
            self.balance=rem+self.balance
            self.loan=amount-self.loan-rem
        print("You overpayed your loan. The remaining amount will be carried forward.")


    def give_loan_dates(self):
        for x in self.loans:
            time=x["time"]
            amount=x["amount"]
            print("Date {}, you acquired a loan of Kshs{}".format(time.strftime("%A, %d, %B, %Y"),amount))

    def repay_loan_dates(self):
        for x in self.repayloan:
            time=x["time"]
            amount=x["amount"]
            print("Date {} you paid your loan{}.".format(time.strftime("%A, %d, %B, %Y"),amount))


    def statement(self):
        for y in self.deposits:
            time=y["time"]
            formated=time.strftime("%A %d %B %Y")
            amount=y["amount"]
            print("On {} you deposited {}".format(formated,amount))

        for y in self.withdrawals:
            time=y["time"]
            formated=time.strftime("%A %d %B %Y")
            amount=y["amount"]
            print("On {} you withdrew {}".format(formated,amount))
            
        for x in self.loan:
            time=x["time"]
            amount=x["amount"]
            print("Date {}, you acquired a loan of Kshs{}".format(time.strftime("%A, %d, %B, %Y"),amount))

        for x in self.repayloan:
            time=x["time"]
            amount=x["amount"]
            print("Date {} you paid your loan{}.".format(time.strftime("%A, %d, %B, %Y"),amount))

