nums_str_comma = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
print(f'Оригинальная строка: {nums_str_comma}')

nums_int = nums_str_comma.split(', ')
nums_str_space = " ".join(nums_int)
print('Строка с изменённым разделителем: {}'.format(nums_str_space))