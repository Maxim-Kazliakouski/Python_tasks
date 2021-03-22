# # ---- Task 1 ----
# s = 'Перестановочный алгоритм быстрого действия'
# i = 0
# for str_elem in s:
#     if str_elem == 'о':
#         i = i+1
#         print(str_elem, end=' ')
# print('\n''There are {} symbols "o"'.format(i))
#
# # ---- Task 2 -----
# s = 'Перевыборы выбранного президента'
# i = 0
# for str_elem in s:
#     if str_elem == 'е':
#         i = i+1
#         print(str_elem, end=' ')
# print('\n''There are {} symbols "е"'.format(i))

# ---- Task 3 -----
s = 'Посмотрите как Рите нравится ритм'
s1 = s.lower()
dlina = len(s1)
print(dlina)
i = 0
for ch in range(0, len(s1)-2):
    x = s1.find('рит', i, i+3)
    if x != -1:
        print(s1.index('рит', i, i+3))
    i += 1
# ss = 'рит'
# str_elem = s1.index(ss)
# while str_elem < len(s1):
#     print(s1.index(ss, str_elem))
#     str_elem = s1.index(ss, str_elem+1)



