adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3


# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"\ntask 01 == Текст без зайвих абзаців:\n{adwentures_of_tom_sawer}\n")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", "")
print(f"task 02 == Текст без зайвих крапок:\n{adwentures_of_tom_sawer}\n")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"task 03 == Текст без зайвих пробілів:\n{adwentures_of_tom_sawer}\n")


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f"task 04 == Літера 'h' зустрічається: {adwentures_of_tom_sawer.count("h")} разів\n")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
splited_text = adwentures_of_tom_sawer.split()
count_titled = 0
for i in splited_text:
    if i.istitle():
        count_titled += 1
print(f"task 05 == Кількість слів з Великої букви: {count_titled}\n")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_Tom_index = adwentures_of_tom_sawer.find("Tom")
second_Tom_index = adwentures_of_tom_sawer.find("Tom", first_Tom_index + 1)
print(f"task 06 == Позиція на якій слово Tom, зустрічається другий раз: {second_Tom_index}\n")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.strip(".").split(".")
print(f"task 07 == Змінна adwentures_of_tom_sawer_sentences розділена на список:\n{adwentures_of_tom_sawer_sentences}\n")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"task 08 == Четверте речення: {adwentures_of_tom_sawer_sentences[3]}")
print(f"Перетворений рядок у нижній регістр: {adwentures_of_tom_sawer_sentences[3].lower()}\n")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(f"task 09 == Шукаємо речення яке починається з 'By the time':")
count = 0
for i in adwentures_of_tom_sawer_sentences:
    count += 1
    if i.strip().startswith("By the time"):
        print(f"Речення номер {count} починається з 'By the time'\n")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(f"task 10 == Кількість слів останнього речення: {len(last_sentence.split())}")