from pydal import DAL, Field # https://github.com/web2py/pydal
db = DAL('sqlite://ccaccounts.db')
db.define_table('accounts',
                Field('name'),
                Field('account_number', 'integer'),
                Field('balance', 'integer'),
                Field('balance_limit', 'integer'))


class AccountManager:

    def __init__(self, name, account_number, balance_limit):
        if name: # check for null string in name parameter
            if account_number > 0 and balance_limit > 0: # check that non zero or negative numbers are being passed
                self.name = name                         # in the account number or in the balance limit
                self.account_number = account_number
                self.balance = balance_limit
                self.balance_limit = balance_limit
                self.add(name, account_number, balance_limit) # add the account to the DB if the conditions are met
            else:
                raise SyntaxError("""Check your parameters for invalid account number/balance limit value
        (examples. negatives or non-numbers)""")
        else:
            raise SyntaxError("ERROR: Check your parameters for null name")

    def add(self, name, account_number, balance_limit):
        # checks if account name and account number already exist in the DB
        if db(db.accounts.name == name).count() > 0 or db(db.accounts.account_number == account_number).count() > 0:
            raise ValueError("ERROR: This account name/number already exists")
        else:
            db.accounts.insert(name=name,
                               account_number=account_number,
                               balance=balance_limit,
                               balance_limit=balance_limit)
            db.commit()

    def charge(self, name, amount):
        pass
    def credit(self, name, amount):
        pass