# ---- ATM ----
users = {'Max': 'Kazliakouski', 'Natallia': 'Kazliakouskaya'}
pin_codes = {'Max': '0509', 'Natallia': '0505'}
cash = {'Max': 100, 'Natallia': 200}


class ATM:
    def __init__(self, first_name=input('First name: '),
                 last_name=input('Last name: ')):
        self.first_name = first_name
        self.last_name = last_name

    def user_initialization(self):
        access = None
        if self.first_name in users.keys() and self.last_name in users.values():
            print(f'The full name of user is {self.first_name} {self.last_name}')
            access = True
        else:
            print('There is no such users!')
        return access

    def verifying_pin_code(self, pin_code):
        self.pin_code = pin_code
        attempts = 0
        if self.pin_code == pin_codes[self.first_name]:
            print('Correctly Pin-code')
        else:
            while self.pin_code != pin_codes[self.first_name]:
                print('You enter invalid pin-code...')
                attempts += 1
                self.pin_code = input('Enter Pin-code again: ')
                if self.pin_code == pin_codes[self.first_name]:
                    print('Correctly PIN-code!')
                    break
                if attempts > 1:
                    print('Your card is blocked')
                    break

    def popolnenie_scheta(self):
        suma_popolnenia = int(input('Enter cash amount for adding: '))
        cash[self.first_name] = suma_popolnenia + cash[self.first_name]
        # print(cash[self.first_name])

    def snytie_cash(self):
        suma_snytiya = int(input('Enter cash amount for minus: '))
        cash[self.first_name] = cash[self.first_name] - suma_snytiya

    def ostatok(self):
        print(f'Current sum is {cash[self.first_name]} $')


# user1 = ATM()
# if user1.user_initialization():
#     user1.verifying_pin_code(input('Pin-code: '))
# else:
#     print('Access denied!')

# user1.popolnenie_scheta()
# user1.snytie_cash()
# user1.ostatok()
