# ---- Task 3 ----
price = {'menu_1': 12.00, 'menu_2': 13.40}


class Lunch:
    def __init__(self, menu):
        self.menu = str(menu)

    def menu_price(self, choice=int(input('Make your menu choice: '))):
        if choice == 1:
            print(f'Your choice is {choice}', end='\nThe price is: {}$'.format(price['menu_1']))
        elif choice == 2:
            print(f'Your choice is {choice}', end='\nThe price is: {}$'.format(price['menu_2']))
        else:
            print('Error menu')


Paul = Lunch('Menu 1')
Paul.menu_price()

# ---- Task 4 ----


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point.__repr__())

from Task8 import ATM

user1 = ATM()
if user1.user_initialization():
    user1.verifying_pin_code(input('Pin-code: '))
else:
    print('Access denied!')

