"""
In this project, I created a Python class that can be used to create and manipulate a personal bank account.
"""

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return "%s's account. Current balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    print("$%.2f" % (self.balance))
    
  def deposit(self, amount):
    if amount <= 0:
      print("The deposit amount can not be zero or less.")
    else: 
      print("You've deposited $%.2f." % (amount))
      self.balance += amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print("You do not have enough in your account for that withdraw.")
    else:
      print("You've withdrawn $%.2f." % (amount))
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Barbie")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
