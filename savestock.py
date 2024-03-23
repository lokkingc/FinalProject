version = 1.0
description = 'Save stock data to csv file'
usage = f'{command} <filename.csv>'

def run(filename):
    with open(filename, 'w', newline='') as f:
        dw = csv.writer(f)
        fieldnames = ['name', 'price', 'quanity']
        result = cursor.execute('select * from Stock')
        dw.writerow(fieldnames)
        for row in result:
            dw.writerow(list(row))
    return 'Saved stock data'

def check(*args):
    return len(args) == 1