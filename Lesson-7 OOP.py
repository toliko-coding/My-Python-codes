# --------------------------------------
# dispatch function 
# --------------------------------------
'''
def make_account(balance, owner):
    """Return a dispatch function that represents a bank account."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance
    def get_balance():
        return balance
    def get_owner():
        return owner
    def dispatch(msg):
        if msg == 'withdraw':
            return withdraw
        elif msg == 'deposit':
            return deposit
        elif msg == 'get_balance':
            return get_balance
        elif msg == 'get_owner':
            return get_owner
    return dispatch
'''
# --------------------------------------
'''
>>> a = make_account(100, 'M')
>>> a('get_owner')()
'M'
>>> a('get_balance')()
100
>>> a('withdraw')(20)
80
'''

# --------------------------------------
# dispatch dictionary
# --------------------------------------
'''
def make_account(balance, owner):
    """Return a dispatch function that represents a bank account."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance
    def get_balance():
        return balance
    def get_owner():
        return owner
    dispatch = {'withdraw': withdraw, 'deposit': deposit,
                'get_balance': get_balance, 'get_owner': get_owner}
    return dispatch
'''
# --------------------------------------
'''
>>> a = make_account(100, "M")
>>> a["get_owner"]()
'M'
>>> a['get_balance']()
100
>>> a['withdraw'](20)
80
'''

# --------------------------------------
# OOP
# --------------------------------------
'''
class Account(object):
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
'''
# --------------------------------------
'''
>>> tom_account = Account('Tom')
>>> tom_account.deposit(100)
100
>>> tom_account.withdraw(90)
10
>>> tom_account.withdraw(90)
'Insufficient funds'
>>> tom_account.holder
'Tom'
'''
# --------------------------------------
'''
>>> getattr(tom_account, 'balance')
10
>>> hasattr(tom_account, 'deposit')
True
>>> type(Account.deposit)
<class 'function'>
>>> type(tom_account.deposit)
<class 'method'>
>>> Account.deposit.__code__ == tom_account.deposit.__code__
True
'''
# --------------------------------------
'''
>>> Account.deposit(tom_account, 1001)
1011
>>> getattr(Account,'deposit')(tom_account, 1001)
2012
>>> tom_account.deposit(1000)
3012
>>> getattr(tom_account,'deposit')(1000)
4012
'''
# --------------------------------------
# Class attributes
# --------------------------------------
'''
class Account(object):
    interest = 0.02 # A class attribute
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
	# Additional methods would be defined here
'''
# --------------------------------------
'''
>>> tom_account = Account('Tom')
>>> jim_account = Account('Jim')
>>> tom_account.interest
0.02
>>> jim_account.interest
0.02
>>> Account.interest = 0.04
>>> tom_account.interest
0.04
>>> jim_account.interest
0.04
>>> jim_account.interest = 0.08
>>> jim_account.interest
0.08
>>> tom_account.interest
0.04
>>> Account.interest = 0.05
>>> tom_account.interest
0.05
>>> jim_account.interest
0.08
>>> Account.stam = 0
>>> Account.stam
0
>>> Account.func = lambda x: 5
>>> Account.func(2)
5
>>> a = Account('Sam')
>>> a.func()
5
'''

# --------------------------------------
# Using Inheritance
# --------------------------------------
'''
class Account(object):
    """A bank account that has a non-negative balance."""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
'''
# --------------------------------------
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)
# --------------------------------------
'''
>>> checking = CheckingAccount('Sam')
>>> checking.deposit(10)
10
>>> checking.withdraw(5)
4
>>> checking.interest
0.01
'''
# --------------------------------------
# Multiple Inheritance
# --------------------------------------
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)
# --------------------------------------
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # A free dollar!
# --------------------------------------
'''
>>> such_a_deal = AsSeenOnTVAccount("John")
>>> such_a_deal.balance
1
>>> such_a_deal.deposit(20)
19
>>> such_a_deal.withdraw(5)
13
>>> such_a_deal.deposit_charge
2
>>> such_a_deal.withdraw_charge
1
[c.__name__ for c in AsSeenOnTVAccount.mro()]
['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
'''
