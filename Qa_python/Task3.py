# ------ Task 1 ------
a, b = 10, 15
if a == b:
    print('The values are equal')
elif a < b:
    print('The value a < b')
elif a > b:
    print('The value b < a')

# ------ Task 2 ------

a, b = 10, 15
summa = a + b
if summa%2 == 0:
    print('Maybe a and b are even')
else:
    print('Some variable is odd')

# ----- Task 3 -----

a = 3
div_by_two = int(a/2)
print('Value a = {}'.format(a))
if a > 10:
    print('Value {} > 10'.format(a))
else:
    print('Value {} < 10'.format(a))

if a < 100:
    print('Value {} < 100'.format(a))
else:
    print('Value {} > 100'.format(a))

if a/2 > 20:
    print('The result of division value {} on 2 will be'.format(a) + div_by_two)
else:
    print('The condition of division by 2 does not performed...', div_by_two, '< 20')

if 5 <= a <= 40:
    print('The value {} in range between 5 and 40'.format(a))
elif a < 5:
    print('The value {} < 5'.format(a))
elif a > 40:
    print('The value {} > 40'.format(a))
else:
    print(('The value {} is not in range between 5 and 40'.format(a)))
