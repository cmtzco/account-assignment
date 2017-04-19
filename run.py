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
        acct = AccountManager()
        acct.charge(name, amount)

    elif operation == 'credit' and len(group) == 3:
        name = group[1]
        amount = int(group[2])
        acct = AccountManager()
        acct.credit(name, amount)

    else:
        pass

acct.balances()




# john = AccountManager("John", 123456, 1000)
# flerm = AccountManager("Schmerpmer", 2341123, 12323)
# flerm = AccountManager("FlimFlams", 50, 23416)
# flerm.add()
# flerm.charge("FlimFlams", 550)
# flerm.credit("FlimFlams", 21000)