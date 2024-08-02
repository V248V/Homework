# 1
def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(4)
print_params(4, 2)
print_params(4, 2, 3)
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2
values_list = [5, 'space', True]
values_dict = {'a': 10, 'b': 'anything', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)