my_dict = {'Ivan': 1990, 'Kris': 2000, 'Kirill': 2001}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Katya'))
my_dict.update({'Egor': 1995,
                'Sasha': 1999})
deleted_name = my_dict.pop('Kris')
print(deleted_name)
print(my_dict)

my_set = {1, 1, 2, 2, 'String', 'String', 4.55, 4.55}
print(my_set)
my_set.add('New String')
my_set.add(6561)
my_set.discard('String')
print(my_set)