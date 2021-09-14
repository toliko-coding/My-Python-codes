    """Return a new class (a dispatch dictionary) with given class attributes"""
    #print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value

        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls


### class Account
# The Account class is created through a make_account_class function,
# which has structure similar to a class statement in Python,
# but concludes with a call to make_class.
def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    def __init__(self, holder):
        self['set']('holder', holder)
        self['set']('balance', 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self['set']('balance', self['get']('balance') + amount)
        return self['get']('balance')

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    #print(locals())
    # locals() returns a dictionary of local variables
    return make_class(locals())


Account = make_account_class()
jim_acct = Account['new']('Jim')

print(jim_acct['get']('holder'))         # Jim
print(jim_acct['get']('interest'))       # None
print(jim_acct['get']('deposit')(20))    # 20
print(jim_acct['get']('withdraw')(5))    # 15
print(jim_acct['set']('interest', 0.04)) # None
print(jim_acct['get']('interest'))       #0.04
print(Account['get']('interest'))        # None


### class CheckingAccount, inheriting from Account
def make_checking_account_class():
    #Return the CheckingAccount class, which imposes a $1 withdrawal fee.
    interest     = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)

    return make_class(locals(), Account)


CheckingAccount = make_checking_account_class()
jack_acct = CheckingAccount['new']('Jack')
print(jack_acct['get']('interest'))    # 0.01
print(jack_acct['get']('deposit')(20)) # 20
print(jack_acct['get']('withdraw')(5)) # 14


