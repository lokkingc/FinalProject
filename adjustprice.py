version = 1.0
description = 'adjust price'
usage = f'{command} <name> <price>'

def run(name, price):
    cursor.execute('update Stock set price=? where name=?', (price, name))
    return ('Price changed')

def check(*args):
    return len(args) == 2