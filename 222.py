lis = {"name": {"first_name": "Max", "last_name": "Kazliakouski"},
       "address": {"first_address": "Minsk", "second_address": "Pinsk"}, "phone": [+375298248359, +375259444181]}
print(lis["name"]["last_name"], lis["address"]["first_address"], lis["phone"][0])


def message(b, c):
    a = b + c
    return print("Function returns:", a)


message(2, 3)


