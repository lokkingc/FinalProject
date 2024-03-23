version = 1.0
description = 'remove item based on price'
usage = f'{command} <name>'

def run(name):
    cursor.execute('delete from Stock where name=?', (name))
    return 'Deleted'

def check(*args):
    return len(args) == 2