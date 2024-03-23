version = 1.0
description = 'get price and quantity of one product'
usage = f'{command} <name>'

def run(name):
    result = cursor.execute('select * from Stock where name like :name', {'name': name})
    item = result.fetchall()
    return (f'Price: {item[0][1]}\nQuantity: {item[0][2]}')

def check(*args):
    return len(args) == 1