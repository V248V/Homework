list_1 = []                 # создаю список для чисел из 1 вствки
for i in range(3, 21):
    list_1.append(i)

pairs_of_numbers_1 = []     # создаю два списка для перебора сумм
pairs_of_numbers_2 = []
for i in range(1, 21):
    pairs_of_numbers_1.append(i)
    pairs_of_numbers_2.append(i)

def devidedby(number):
    res = ''                     # строка для вывода ответа
    for i in pairs_of_numbers_1:
        for j in pairs_of_numbers_2:
            if number % (i + j) == 0 and i != j:
                res = res + str(i) + str(j)
        pairs_of_numbers_2.remove(i)
    for u in range(1, 21):      # заново заполняю 2 список, так как он пустой после 1 итерации
        pairs_of_numbers_2.append(u)
    return res

for k in range(3, 21):
    result = devidedby(k)
    print(result)