# 2023/10/01 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While."
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    a = my_list[i]
    if a > 0:
        print(a)
    elif a < 0:
        break
    i += 1