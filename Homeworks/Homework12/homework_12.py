def sum_square_sea(first_sea, second_sea):
    return first_sea + second_sea

def count_parni(lst):
    parni = []
    for i in lst:
        if i == 0:
            continue
        elif i % 2 == 0:
            parni.append(i)
    return len(parni)

def string_item_count(lst):
    lst2 = []
    for i in lst:
        if type(i) == str:
            lst2.append(i)
    if lst2:
        return len(lst2)
    else:
        return "Список немає елементів str"

def count_computer_price(month_count, money_per_month):
    total_cost = month_count * money_per_month
    return total_cost