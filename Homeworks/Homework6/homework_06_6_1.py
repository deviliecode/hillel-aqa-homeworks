string_1 = input("Enter your string: ")

uniq = []

for i in string_1:
    if string_1.count(i) == 1:
        uniq.append(i)

print(len(uniq) > 10)
