# list +
# list_a = list(range(8))
# print(list_a)
#
# print(list_a[-1])
#
# a = 23
# b = 10
# print(f'{a+b}')


from Task8 import ATM


class New(ATM):
    pass


user1 = New()
if user1.user_initialization():
    user1.verifying_pin_code(input('Pin-code: '))
else:
    print('Access denied!')
