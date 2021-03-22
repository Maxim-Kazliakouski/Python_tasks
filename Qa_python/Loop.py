# Циклы

list_var = ['first', 'second', 'third']

# for <var> in <list>
# 1. var = list[0]
# print(var)

for element in list_var:
    print(element)
    if element == 'second':
        print('few more actions')

str_var = 'best test ever'
for char in str_var:
    print(char, end='\n')

dict_var = {'first': 1, 'second': 2, 'third': 3}
# items преобразовывает словарь, чтобы мы могли присваивать одновременно их значения из словаря
for key, value in dict_var.items():
    # key, value = 'first', 1 т.е. идёт попарное присвоение переменных  key = first, value = 1
    print('key: {}'.format(key))
    print('value: {}'.format(value))

# другой формат вывода ключ и значение
for key in dict_var.keys():
    print(key)
dict_var['fourth'] = 4
for values in dict_var.values():
    if values == 4:
        print('Value = {} - Victory!!!'.format(values))
    else:
        print('Value = {} - not yet'.format(values))

# пример для метода .format
var1, var2 = 5, 8

print('var1 = {}'.format(var1))
print('var2 = {}'.format(var2))

