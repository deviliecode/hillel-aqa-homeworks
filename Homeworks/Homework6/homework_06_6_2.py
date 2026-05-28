while True:
    word = input("Введіть слово: ")

    if "h" in word.lower():
        print("Є літера h")
        break
    else:
        print("У слові немає літери h")