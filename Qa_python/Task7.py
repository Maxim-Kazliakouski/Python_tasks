# ---- Exercise_1 -----
inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
             'pocket': ('seashell', 'strange berry', 'lint')}
d = []
for key in inventory:
    if key == 'backpack':
        a = inventory[key]
# Возвращение отсортированного списка
print(sorted(a))
# удаление последнего элемента из списка
a.remove('dagger')
print(sorted(a))
#  добавление +50 к значению 'gold'
for key in inventory:
    if key == 'gold':
        c = int(inventory[key]) + 50
        inventory['gold'] = c
print(inventory)

# ---- Exercise_2 ----
prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3
stock = 3
print(prices)
for key, values in prices.items():
    print('Fruit - ' + '{}'.format(key).upper())
    print('Price = {}$'.format(values))
    print('Stock = {}'.format(stock))
# print(prices.values())
total = 0
for each_price in prices.values():
    x = each_price*stock
    total = total + x
print('The full price is - {}$'.format(total))







