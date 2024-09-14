from pprint import pprint
def custom_write(file_name, strings):
    string_positions = {}
    string_num = 1
    name = file_name
    file = open(name, 'w', encoding='utf-8')

    for i in strings:
        byte_i = file.tell()
        string_positions[(string_num, byte_i)] = i
        string_num += 1
        file.write(str(i))
        file.write('\n')

    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)