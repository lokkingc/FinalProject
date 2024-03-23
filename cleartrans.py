version = 1.0
description = 'clear transaction history'
usage = f'{command}'

def run():
    result = cursor.execute('delete from Transactions')
    return "Cleared"

def check(*args):
    return len(args) == 0