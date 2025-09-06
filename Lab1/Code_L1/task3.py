# clear method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }
print('Оригинальный словарь: ', fruit_prices)
fruit_prices.clear()
print('Очищенный словарь: ', fruit_prices)
print()

# copy method
fruit_prices_1 = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }
fruit_prices_2 = fruit_prices_1.copy()

key = 'apple'
fruit_prices_1[key] = 100
print('Цена фрукта %s в словаре 1: %d' % (key, fruit_prices_1[key]))
print('Цена фрукта %s в словаре 2: %d' % (key, fruit_prices_2[key]))
print()

# fromkeys method
fruits = ['apple', 'banana', 'orange', 'grape', 'lemon', 'pear', 'kiwi', 'mango', 'pineapple', 'watermelon']
fruit_prices = dict.fromkeys(fruits, 100)
print('Цены фруктов: ', fruit_prices)
print()

# get method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }
# print(fruit_prices['grapefruit']) # Приводит к исключению KeyError
print(fruit_prices.get('grapefruit', 'Нет в продаже'))
print()

# keys method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }

product = 'Фрукты: '
for key in fruit_prices.keys():
    product += f'{key}, '
product = product.rstrip(', ')
print(product)
print()

# values method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }

product = 'Цены фруктов: '
for value in fruit_prices.values():
    product += f'{value}, '
product = product.rstrip(', ')
print(product)
print()

# items method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40, 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70, 'pineapple': 90, 'watermelon': 120 }

product = 'Фрукты и их цены: '
for key, value in fruit_prices.items():
    product += f'{key}: {value}, '
product = product.rstrip(', ')
print(product)
print()

# pop method
fruit_prices = { 'apple': 50, 'banana': 30, 'orange': 40 }
print('Словарь до удаления ключа: ', fruit_prices)
fruit_prices.pop('apple')
print('Словарь после удаления пары ключ-значение по ключу: ', fruit_prices)
print()

# popitem method
fruit_prices = { 'apple': 50, 'banana': 50, 'orange': 40 }
fruit_prices['grape'] = 80
fruit_prices['lemon'] = 25
print('Словарь до удаления последней добавленной пары ключ-значение: ', fruit_prices)
fruit_prices.popitem()
print('Словарь после удаления последней пары ключ-значение: ', fruit_prices)
print()

# setdefault method
fruit_prices = { 'apple': 50, 'banana': 50, 'orange': 40 }
print('Словарь до вызова setdefault() для несуществующего ключа: ', fruit_prices)
print('Значение по умолчанию для нового ключа: ', fruit_prices.setdefault('pear', 60))
print('Словарь после вызова setdefault(): ', fruit_prices)
print()

# update method
fruit_prices = { 'apple': 50, 'banana': 50, 'orange': 40 }
fruit_prices_1 = { 'grape': 80, 'lemon': 25, 'pear': 45, 'kiwi': 60, 'mango': 70 }
print('Оригинальный словарь до обновления: ', fruit_prices)
fruit_prices.update(fruit_prices_2)
print('Оригинальный словарь после обновления: ', fruit_prices)