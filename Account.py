from Connector import Connector
from config import *

class AccountManager:
    # @param name string Name of the account owner
    # @param account_number int Account number
    # @param balance int Account balance
    # return None
    def __init__(self, name="", account_number=0, balance=0, balance_limit=0, amount=0):
        self.connector = Connector()
        if amount > 0:
            self.name = name
            self.amount = amount
        elif type(name) == str and type(account_number) == int and type(balance_limit) == int:
            self.name = name
            self.account_number = account_number
            self.balance = balance
            self.balance_limit = balance_limit
            self.amount = amount
        else:
            if LOGGING_LEVEL == 'INFO':
                pass
            elif LOGGING_LEVEL == 'DEBUG':
                print """Incorrect parameter type, expected types
        name:string, account_number:integer, balance_limit:integer"""
                pass

    # account_check does a count to see if the account name exists
    # @param name string Name of the account owner
    # return Boolean
    def account_check(self, name):
        if self.connector.query_accounts(name):
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
            if self.account_number > 0 and self.balance_limit > 0:
                self.connector.add_account(self.name, self.account_number, self.balance, self.balance_limit)
            else:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print """ERROR: Check your parameters for invalid account number/balance limit value
        (examples. negatives or non-numbers)"""
                    pass

        else:
            if LOGGING_LEVEL == 'INFO':
                pass
            elif LOGGING_LEVEL == 'DEBUG':
                print "ERROR: Check your parameters for null name"
                pass

    # charge increases the account balance based on the amount given
    # @param name string Name of the account owner
    # @param amount int amount to increment the balance by
    # return None
    def charge(self):
        if self.connector.query_accounts(self.name):
            if self.amount > 0:
                self.connector.charge_account(self.name, self.amount)
            else:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print "Amount is negative or 0, value must be greater than 0"
                    pass
        else:
            pass

    # credit decreases the account balance based on the amount given
    # @param name string Name of the account owner
    # @param amount int amount to increment the balance by
    # return None
    def credit(self):
        if self.connector.query_accounts(name=self.name):
            if self.amount > 0:
                self.connector.credit_account(self.name, self.amount)
            else:
                if LOGGING_LEVEL == 'INFO':
                    pass
                elif LOGGING_LEVEL == 'DEBUG':
                    print "Amount is negative or 0, value must be greater than 0"
                    pass
        else:
            pass

    # balances prints out the accounts and balances in the correct format and in alphabetical order
    # return None
    def balances(self):
        self.connector.account_balances()
