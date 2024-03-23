version = 1.0
description = 'clear stock database'
usage = f'{command}'

def run():
    result = cursor.execute('delete from Stock')
    return "Cleared"

def check(*args):
    return len(args) == 0