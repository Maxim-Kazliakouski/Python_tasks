a, b = 10, 15
summa = a + b
multiple = a * b
substraction = b - a
division = b / a
ostatok_ot_delenia = b % a

print('Summa = {}'.format(summa))
print('Multiplication = {}'.format(multiple))
print('Subsctraction = {}'.format(substraction))
print('Division = {}'.format(division))
print('Ostatok = {}'.format(ostatok_ot_delenia))

if a%2 == 0:
    print('Value {} is an even number'.format(a))
else:
    print('Value {} is an odd number'.format(a))

if b%2 == 0:
    print('Value {} is an even number'.format(b))
else:
    print('Value {} is an odd number'.format(b))
    print('Ostatok ot delenia = {}'.format(b%2))
    print("😎")
