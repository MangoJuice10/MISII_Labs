# append method
myList = [1, 2, 3]
print('Исходный список: ', myList)
myList.append(4)
print('Список с единственным добавленным элементом: ', myList, end="\n\n")

# extend method
myList = [1, 2, 3]
print('Исходный список: ', myList)
myList.extend([4, 5, 6])
print('Список с несколькими добавленными элементами: ', myList, end="\n\n")

# insert method
myList = [1, 2, 3, 5, 6, 7]
myNum = 4
print('Исходный список: ', myList)
myList.insert(3, myNum)
print('Список со вставленным элементом %d' % myNum, myList, end="\n\n")

# pop method
myList = [1, 2, 3, 4, 5]
print('Исходный список: ', myList)
myNum = myList.pop()
print('Список без последнего элемента %d: ' % myNum, myList, end="\n\n")

# remove method
myList = [1, 2, 3, 4, 5]
print('Исходный список: ', myList)
myList.remove(2)
print('Список без элемента с индексом 2: ', myList, end="\n\n")

# reverse method
myList = [1, 2, 3, 4, 5]
print('Перевернутый список %s: %s' % (myList, myList.reverse()), end="\n\n")

# sort method
myList = [3, 2, 5, 6, 9, 8, 7, 0, 4, 1]
print('Список до сортировки: ', myList)
myList.sort()
print('Список после прямой сортировки: ', myList)
myList.sort(reverse = True)
print('Список после обратной сортировки: ', myList, end="\n\n")

# count method
haystack = [1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2]
needle = 1
print('Число повторений элемента %d в списке %s: %d' % (needle, str(haystack), haystack.count(needle)), end="\n\n")

# index method
haystack = [1, 2, 3, 5, 1, 5, 2, 7, 8, 9, 0]
needle = 5
print(f'Индекс первого слева элемента со значением {needle} в списке {str(haystack)}: {haystack.index(needle)}', end="\n\n")