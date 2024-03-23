version = 1.0
description = 'add product to current stock'
usage = f'{command} <filename.csv>'

def run(filename):
    with open(filename) as f:
        try:
            dictReader = csv.DictReader(f)
        except Exception:
            print('Please enter csv file')
        try:
            for item in dictReader:
                name = item['Name'].lower()
                price = item['Price']
                quantity = int(item['Quantity'])
                result = cursor.execute('select * from Stock where name like :name', {'name': name})
                list = result.fetchall()
                if not list:
                    cursor.execute('insert into Stock (name, price, quantity) values (?, ?, ?)', (name, price, quantity))
                else:
                    newQuantity = list[0][2]
                    quantity += newQuantity
                    cursor.execute('update Stock set quantity=?, price=? where name=?', (quantity, price, name))
                    #cursor.execute('update Stock set price=? where name=?', (price, name))
        except Exception as e:
            return('Please have column names in this order: Name, price, quantity')
    return 'Added stock'

def check(*args):
    return len(args) == 1

