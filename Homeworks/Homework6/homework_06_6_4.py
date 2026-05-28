lst = [1, 3, 4, 123, 4, 32, 33, 32, 15, 13, 2000, 2001]

parni = []

for i in lst:
    if i % 2 == 0:
        parni.append(i)

print(f"Парних чисел —— {len(parni)}")