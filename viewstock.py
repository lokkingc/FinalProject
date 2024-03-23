version = 1.0
description = 'view current stock'
usage = f'{command}'

def run():
    result = cursor.execute('select * from Stock')
    for row in result:
        print(row)
    return 'End of database'

def check(*args):
    return len(args) == 0