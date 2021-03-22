# class Tools_For_Painting:
#     def who_is_parent(self):
#         print("Parent: tools for painting")
#     pass
#
#
# class ruchki(Tools_For_Painting):
#     pass
#
#
# class kistochki(Tools_For_Painting):
#     def __init__(self, _price):
#         self.my_price = _price
#     def who_is(self):
#         print(f'I am a pen with price {self.my_price}')
#     pass
#
#
# obj1 = kistochki('100$')
# obj1.who_is()
# obj1.who_is_parent()

# class Person:
#     name = 'Ivan'
#     age = 10
#
#     def set(self, name, age):
#         self.name = name
#         self.age = age
#         # print(f'The name of person is {self.name} and age is {self.age}')
#
# name_all = Person()
# name_all.set('Max', 25)

# class Dog:    # Простая модель собаки
#     def __init__(self, name, age):    # инициализируем атрибуты имя и возраст
#         self.name = name
#         self.age = age
#         # print('Собака создана!')
#
#     def sit(self): # Собака будет садиться по команде
#         print(self.name.title() + " собака села")
#
#     def jump(self): # Собака будет прыгать по команде
#         print((self.name.title() + " собака подпрыгнула"))
#
#     def wow(self): # Собака будет гавкать
#         print('Wow-wow-wow')
#
# dog_type = Dog('Max', 5)
# dog_type2 = Dog('Nick', 2)
# Rex = Dog('Rex', 6)
# Rex.wow()

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'The name of restaurant is {self.restaurant_name} and this restaurant has {self.cuisine_type} cuisine')
#
#     def open_restaurant(self):
#         print('Restaurant is open')
#
# restaurant = Restaurant('Friends', 'Belarusian')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

class User:
    def __init__(self, first_name, last_name, user_age, user_gender):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_gender = user_gender

    def describe_user(self):
        print('There is some information about user...')
        print(f"User's first name: {self.first_name}")
        print(f"User's last name: {self.last_name}")
        print(f"User's age: {self.user_age} years old")
        print(f"User's gender: {self.user_gender}")

    def greed_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


Max = User(input('Please, input first name: '),
           input('Please, input last name: '),
           int(input('Please, input age: ')),
           input('Please, input gender: '))
print()
Max.greed_user()
Max.describe_user()
# print()
# Natallia = User('Natallia', 'Kazliakouskaya', 24, 'female')
# Natallia.greed_user()
# Natallia.describe_user()