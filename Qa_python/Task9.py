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
