immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
# immutable_var[0] = 2
# It is impossible because 'tuple' object does not support item assignment
mutable_list = [1, 2, 'a', 'b']
mutable_list[0] = 5
mutable_list.append('Modified')
print(mutable_list)