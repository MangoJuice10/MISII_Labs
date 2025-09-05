fruits = [
    "Apple",
    "banana",
    "apricot",
    "Grape",
    "avocado",
    "orange",
    "kiwi",
    "Almond",
    "Blueberry",
    "artichoke"
]

count = 0
for i in fruits:
    if i.lower().startswith('a'):
        count += 1

print('''Количество фруктов, название которых начинается с буквы "a": \n%d''' % count)