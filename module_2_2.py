first = input('Введите первое число ')
second = input('Введите второе число ')
third = input('Введите третье число ')
if first == second == third:
    print(3)
elif first == second:   # можно сделать c помощью or, но
    print(2)            # в задании написано лучше расписать
elif second == third:
    print(2)
elif third == first:
    print(2)
else:
    print(0)