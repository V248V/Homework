def add_everything_up(a, b):
    try:
        added = a + b
        return added
    except TypeError:
        text = str(a) + str(b)
        return text

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))