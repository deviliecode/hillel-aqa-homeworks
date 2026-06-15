lst = ["1,2,3,4", "1,2,3,4,50", "qwerty,1,2,3", "1,200,33", "s,22,44", "2,44,554,55"]

def item_sum(array: list):

    for i in array:
        total = 0
        valid = True
        sub_array = i.split(",")
        for k in sub_array:
            try:
                total += int(k)
            except ValueError:
                print("Не можу це зробити!")
                valid = False
                break
        if valid:
            print(total)

item_sum(lst)