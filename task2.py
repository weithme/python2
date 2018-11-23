#2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
#Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

#Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json

def write_order_to_json(item, quantity, price, buyer, date):
    
    dict_to_json = {
        "orders": {
            "item": item,
            "quantity": quantity, 
            "price": price, 
            "buyer": buyer, 
            "date": date
        }
    }
    
    with open(fname, 'w', encoding='utf-8') as f_n:
        #f_n.write(json.dumps(dict_to_json))
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)

fname = 'orders.json'
write_order_to_json ("Арбуз", 2, 20.5, 'Иванов', '20181123')

# Проверка файла
with open(fname) as f_n:
    obj = json.load(f_n)
    for section, commands in obj.items():
        print(section)
        print(commands)

with open(fname) as f_n:
    print(f_n.read())
