lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for i in lst1:
    if type(i) == str:
        lst2.append(i)

if lst2:
    print(f"Список lst2 має {len(lst2)} елементів з типом str")
else:
    print("Список lst2 НЕмає змінних з типом str")
