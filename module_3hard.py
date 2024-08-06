data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35,))}])
]


def calculate_structure_sum(data_structure):
    sum_all = 0
    for item in data_structure:
        if isinstance(item, list):
            sum_all += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for keys, values in item.items():
                if isinstance(keys, str):
                    sum_all += len(keys)
                if isinstance(values, (int, float)):
                    sum_all += values
                else:
                    sum_all += calculate_structure_sum(item)
        elif isinstance(item, tuple):
            sum_all += calculate_structure_sum(item)
        elif isinstance(item, set):
            sum_all += calculate_structure_sum(item)
        elif isinstance(item, str):
            sum_all += len(item)
        elif isinstance(item, int):
            sum_all += item
    return sum_all


result = calculate_structure_sum(data_structure)
print(result)