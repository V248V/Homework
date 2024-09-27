from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everyting(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')

    return write_everyting


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Еще вариант')
print(first_ball())
print(first_ball())
print(first_ball())
