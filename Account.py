from pydal import DAL, Field # https://github.com/web2py/pydal
db = DAL('sqlite://ccaccounts.db')
db.define_table('accounts',
                Field('name'),
                Field('account_number', 'integer'),
                Field('balance', 'integer'),
                Field('balance_limit', 'integer'))
LOGGING_LEVEL = 'INFO'

class AccountManager:

    # @param name string Name of the account owner
    # @param account_number int Account number
    # @param balance int Account balance
    # return None
    def __init__(self, name="", account_number=0, balance_limit=0):
        if type(name) == str and type(account_number) == int and type(balance_limit) == int:
            self.name = name
            self.account_number = account_number
            self.balance = balance_limit
            self.balance_limit = balance_limit
        else:
            if LOGGING_LEVEL == 'INFO':
                pass
            elif LOGGING_LEVEL == 'DEBUG':
                print """Incorrect parameter type, expected types
        name:string, account_number:integer, balance_limit:integer"""

    # account_check does a count to see if the account name exists
    # @param name string Name of the account owner
    # return Boolean
    def account_check(self, name):
        if db(db.accounts.name == name).count() == 0:
            if LOGGING_LEVEL == 'INFO':
                pass
            elif LOGGING_LEVEL == 'DEBUG':
                print "ERROR: Account does not exist"
            return False
        else:
            return True

    # add adds an account to the database
    # return None
    def add(self):
        if self.name:  # check for null string in name parameter
            if self.account_number > 0 and self.balance_limit > 0:  # check that non zero or negative numbers are being passed
                                                          # in the account number or in the balance limit

                # checks if account name and account number already exist in the DB and returns error if the account exists
                if db(db.accounts.name == self.name).count() > 0 or db(db.accounts.account_number == self.account_number).count() > 0:
                    if LOGGING_LEVEL == 'INFO':
                        pass
                    elif LOGGING_LEVEL == 'DEBUG':
                        print "ERROR: This account name/number already exists"
                else:
                    # inserts the row into the DB with the balance limit as the initial balance.
                    db.accounts.insert(name=self.name,
                                       account_number=self.account_number,
                                       balance=self.balance_limit,
                                       balance_limit=self.balance_limit)
                    db.commit()
            else:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print """ERROR: Check your parameters for invalid account number/balance limit value
        (examples. negatives or non-numbers)"""

        else:
            if LOGGING_LEVEL == 'INFO':
                pass
            elif LOGGING_LEVEL == 'DEBUG':
                print "ERROR: Check your parameters for null name"

    # charge increases the account balance based on the amount given
    # @param name string Name of the account owner
    # @param amount int amount to increment the balance by
    # return None
    def charge(self, name, amount):
        if self.account_check(name):
            # find row that matches the name given to do a check on balance limits
            for row in db(db.accounts.name == name).select(db.accounts.balance, db.accounts.balance_limit):
                account_limit = row.balance_limit
                balance = row.balance
            # get the sum of the balance and amount charged
            new_balance = int(amount) + int(balance)
            # make sure the balance will not exceed the balance limit.
            if new_balance > account_limit:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print "Not updating due to surpassing account limit"
            else:
                db(db.accounts.name == name).update(balance=new_balance)
                db.commit()

    # credit decreases the account balance based on the amount given
    # @param name string Name of the account owner
    # @param amount int amount to increment the balance by
    # return None
    def credit(self, name, amount):
        if self.account_check(name):
            # find row that matches the name given to do a check on balance limits
            for row in db(db.accounts.name == name).select(db.accounts.balance, db.accounts.balance_limit):
                account_limit = row.balance_limit
                balance = row.balance
            # get the difference of the balance and amount credited
            new_balance = int(balance) - int(amount)
            # make sure the balance will not go into negatives with the amount credited
            if new_balance < 0:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print "Not updating due to surpassing the balance and causing negative"
            else:
                db(db.accounts.name == name).update(balance=new_balance)
                db.commit()

    # balances prints out the accounts and balances in the correct format and in alphabetical order
    # return None
    def balances(self):
        for row in db().select(db.accounts.name,
                                db.accounts.account_number,
                                db.accounts.balance,
                                orderby=db.accounts.name):
            name = row.name
            acct_number = row.account_number
            balance = row.balance
            print "{}, {}: {}".format(name, acct_number, balance)

