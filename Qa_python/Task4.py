# ----- Task 1 ------
number_list = list(range(0, 16))
for element in number_list:
    print(element, end=' ')

# ----- Task 2 -----
a = 5
stepen = list(range(0, 10))
for ele_step in stepen:
    # if ele_step % 2 > 0 and a**ele_step <= 100000:
    if ele_step >= 0 and a**ele_step <= 10000:
        print('Value a = {}'.format(a), 'in stepen {}'.format(ele_step), end=' ')
        print('is equal', a**ele_step)

# ----- Task 3 -----
new_numbers = list(range(0, 101))
for number in new_numbers:
    if number%4 == 0 and 40 <= number <= 60:
        print('This value {} even number 4'.format(number))

