from pydal import DAL, Field  # https://github.com/web2py/pydal
from Logging import Logger
import config as c

class Connector:

    def __init__(self):
        self.conn_type = c.CONNECTOR_TYPE
        self.log = Logger()
        if self.conn_type == 'DB':
            self.conn = DBConnector()
        else:
            self.log.log_message('NCS')

    def query_accounts(self, name):
        if self.conn_type == 'DB':
            return self.conn.check_accounts(name)
        else:
            self.log.log_message('NCS')


    def add_account(self, name, account_number, balance, balance_limit):
        if self.conn_type == 'DB':
            self.conn.add_account(name, account_number, balance, balance_limit)
        else:
            self.log.log_message('NCS')

    def remove_record(self):
        pass

    def charge_account(self, name, amount):
        if self.conn_type == 'DB':
            self.conn.charge_account(name, amount)
        else:
            self.log.log_message('NCS')

    def credit_account(self, name, amount):
        if self.conn_type == 'DB':
            self.conn.credit_account(name, amount)
        else:
            self.log.log_message('NCS')

    def account_balances(self):
        if self.conn_type == 'DB':
            self.conn.account_balances()
        else:
            self.log.log_message('NCS')


class DBConnector:

    def __init__(self):
        self.db = DAL('sqlite://ccaccounts.db')
        self.db.define_table('accounts',
                        Field('name'),
                        Field('account_number', 'integer'),
                        Field('balance', 'integer'),
                        Field('balance_limit', 'integer'))
        self.log = Logger()

    def check_accounts(self, name):
        if self.db(self.db.accounts.name == name).count() == 0:
            self.log.log_message('NAE')
            return False
        else:
            return True

    def add_account(self, name, account_number, balance, balance_limit):
        # check that non zero or negative numbers are being passed
        # in the account number or in the balance limit

        # checks if account name and account number already exist
        # in the DB and returns error if the account exists
        if self.db(self.db.accounts.name == name).count() > 0 or self.db(
                        self.db.accounts.account_number == account_number).count() > 0:
            self.log.log_message('AAE')
        else:
            # inserts the row into the DB with the balance limit as the initial balance.
            self.db.accounts.insert(name=name,
                               account_number=account_number,
                               balance=balance,
                               balance_limit=balance_limit)
            self.db.commit()

    def charge_account(self, name, amount):
        # find row that matches the name given to do a check on balance limits
        for row in self.db(self.db.accounts.name == name).select(self.db.accounts.balance,
                                                                 self.db.accounts.balance_limit):
            account_limit = row.balance_limit
            balance = row.balance

        if 'balance' in locals():
            # get the sum of the balance and amount charged
            new_balance = int(amount) + int(balance)
            # make sure the balance will not exceed the balance limit.
            if new_balance > account_limit:
                self.log.log_message('SAL')
            else:
                self.db(self.db.accounts.name == name).update(balance=new_balance)
                self.db.commit()
        else:
            self.log.log_message('NBRCH')
            pass

    def credit_account(self, name, amount):
        # find row that matches the name given to do a check on balance limits
        for row in self.db(self.db.accounts.name == name).select(self.db.accounts.balance,
                                                                 self.db.accounts.balance_limit):
            balance = row.balance
        if 'balance' in locals():
            # get the difference of the balance and amount credited
            new_balance = int(balance) - int(amount)
            self.db(self.db.accounts.name == name).update(balance=new_balance)
            self.db.commit()
        else:
            self.log.log_message('NBRCR')
            pass

    def account_balances(self):
        if __name__ == '__main__':
            for row in self.db().select(self.db.accounts.name,
                                   self.db.accounts.account_number,
                                   self.db.accounts.balance,
                                   orderby=self.db.accounts.name):
                name = row.name
                acct_number = row.account_number
                balance = row.balance
                print "{}, {}: {}".format(name, acct_number, balance)


# TODO
# Build Flat File connector class for secondary approach at data source
