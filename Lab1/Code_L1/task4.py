myList = [ "Hello", "world", "PYTHON", "programming", "TEST", "string", "AaBbCc", "lowercase", "UPPERCASE", "mixedCASE", "short", "verylongword", "123456", "abc", "ABCDEFGH" ]

resList = [x for x in myList if len(x) > 5 and x == x.lower()]
print('Исходный список: ', myList)
print('Новый список: ', resList)