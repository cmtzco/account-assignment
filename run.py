from Account import AccountManager
import fileinput

for line in fileinput.input():
    group = line.split()
    operation = group[0].lower()

    if operation == 'add' and len(group) == 4:
        name = group[1]
        account_number = int(group[2])
        balance_limit = int(group[3])
        acct = AccountManager(name=name, account_number=account_number, balance_limit=balance_limit)
        acct.add()

    elif operation == 'charge' and len(group) == 3:
        name = group[1]
        amount = int(group[2])
        acct = AccountManager(name=name, amount=amount)
        acct.charge()

    elif operation == 'credit' and len(group) == 3:
        name = group[1]
        amount = int(group[2])
        acct = AccountManager(name=name, amount=amount)
        acct.credit()

    else:
        pass

acct.balances()

