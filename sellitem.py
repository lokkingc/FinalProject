version = 1.0
description = 'sell products'
usage = f'{command} <name> <quantity> <date>'

def run(name, quantity, date):
    try:
        result = cursor.execute('select * from Stock where name like :name', {'name': name})
        list = result.fetchall()
        newQuantity = list[0][2] - int(quantity)
        if (newQuantity < 0):
            raise Exception
        else:
            cursor.execute('update Stock set quantity=? where name=?', (newQuantity, name))
            cursor.execute('insert into Transactions (date, name, quantity) values (?, ?, ?)', (date, name, quantity))
            return('Sold!')
    except Exception as e:
        return('Not enough stock')
        

def check(*args):
    return len(args) == 3