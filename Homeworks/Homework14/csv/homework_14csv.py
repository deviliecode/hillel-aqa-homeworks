import csv

file1_rows = []
with open("random.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        file1_rows.append(row)

file2_rows = []
with open("random-michaels.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "" in row:
            del row[""]
        file2_rows.append(row)

all_rows = file1_rows + file2_rows

unique_rows = []
for row in all_rows:
    if row not in unique_rows:
        unique_rows.append(row)

with open("without_duplicates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=unique_rows[0].keys())
    writer.writeheader()
    writer.writerows(unique_rows)

print("Всього рядків в обох файлах:", len(all_rows))
print("Унікальних рядків додано у новий файл:", len(unique_rows))
print("Видалено дублікатів:", len(all_rows) - len(unique_rows))