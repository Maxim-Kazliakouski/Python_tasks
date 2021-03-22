# ---- List ----
list_null = list()
list_null1 = []
list_int = [1, 2, 3]


print(list_int.__class__)
print(list_int[0].__class__)

print(bool(list_null1))
# Добавление переменной в список
list_mixed = []
list_mixed.append('First')
print(list_mixed)
print(list_mixed[0])

list_mixed.append('Second')
print(list_mixed)
print(list_mixed[1])
list_mixed[1] = None

# Присваивать можно любой тип переменной
list_mixed[0] = 5
print(list_mixed)
print(list_mixed[0])

# Длина списка
list_length = len(list_mixed)
print(list_length)

# ---------------
str_var = 'test'
str_len = len(str_var)
print(str_var[1])

# ---- Dictionary ----
# По ключу находим значение...
dict_null = dict()
dict_null1 = {}

dict_var = {'string1': 'test1', 'int2': 7}

print(dict_var)
print(dict_var['string1'])
dict_var['string1'] = 'not a string'
print(dict_var)
dict_var['new key'] = 'new value'
print(dict_var)

# Проверка наличия занчения по ключу без ошибки
print(dict_var.get('unknown'))

# Длина словаря
dict_len = len(dict_var)
print(dict_len)

# Вывод ключей и значений
dict_keys = dict_var.keys()
print(dict_keys)
dict_values = dict_var.values()
print(dict_values)
