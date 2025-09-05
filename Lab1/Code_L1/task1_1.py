nums_str = '0 1 2 3 4 5 6 7 8 9'
print('Оригинальная строка: %s' % nums_str)

nums_int = nums_str.split()

nums_inc = [int(num) + 1 for num in nums_int]

print('Обработанная последовательность: ', end = "")
for num in nums_inc:
    print(num, end = " ")