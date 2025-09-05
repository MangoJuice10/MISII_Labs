# format method
print('Это пример {} текста с помощью метода {}.'.format('форматирования', 'format()'))

# strip method
print('   Это пример удаления пробелов в начале и конце строки       '.strip())

# lstrip method
print('   Это пример удаления пробелов в начале строки'.lstrip())

# rstrip method
print('''Это пример удаления символов "_abc" в конце строки_abc_abc_abc_abc'''.rstrip('_abc'))

# capitalize method
print('эТО ПРИМЕР ИЗМЕНЕНИЯ СТРОКИ, ПРИ КОТОРОМ ТОЛЬКО ЕЁ ПЕРВЫЙ СИМВОЛ ПРОПИСНОЙ'.capitalize())

# title method
print('ЭТО ПРИМЕР ИЗМЕНЕНИЯ СТРОКИ, ПРИ КОТОРОМ ТОЛЬКО ПЕРВЫЙ СИМВОЛ КАЖДОГО ЕЁ СЛОВА ПРОПИСНОЙ'.title())

# index method
print("Индекс подстроки \"ab\" в строке \"bc ab ab ab ab ab ab bc\" с начала строки: %d" % "bc ab ab ab ab ab ab bc".index("ab"))

# rindex method
print("Индекс подстроки \"ab\" в строке \"bc ab ab ab ab ab ab bc\" с конца строки: %d" % "bc ab ab ab ab ab ab bc".rindex("ab"))

# replace method
print('Это dummy замены подстроки в строке'.replace('dummy', 'пример'))

# rsplit method
print('''Это пример разделения строки "1, 2, 3, 4, 5, 6" с конца с ограничением 4:''')
print('1, 2, 3, 4, 5, 6'.rsplit(", ", 4))

# partition method
print('''Это пример раделения строки "abc|def|ghi на 3 части слева с разделителем "|":"''')
print('abc|def|ghi'.partition('|'))

# rpartition method
print('''Это пример разделения строки "abc|def|ghi" на 3 части справа с разделителем "|":''')
print('abc|def|ghi'.rpartition('|'))