version = 1.0
description = 'view transaction history'
usage = f'{command} <startDate> <endDate>'

def run(start, end):
    result = cursor.execute('select * from Transactions where date >= :start and date <= :end', {'start': start, 'end': end})
    for row in result:
        print(row)
    return 'End of transaction history for selected dates'

def check(*args):
    return len(args) == 2