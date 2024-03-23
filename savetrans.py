version = 1.0
description = 'Save transaction data to csv file'
usage = f'{command} <startDate> <endDate> <filename.csv>'

def run(start, end, filename):
    with open(filename, 'w', newline='') as f:
        dw = csv.writer(f)
        fieldnames = ['date', 'name', 'quantity']
        dw.writerow(fieldnames)
        result = cursor.execute('select * from Transactions where date >= :start and date <= :end', {'start': start, 'end': end})
        dw.writerows(result)
    return 'Saved transaction data'

def check(*args):
    return len(args) == 3