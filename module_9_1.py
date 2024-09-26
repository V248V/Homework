def apply_all_func(int_list, *functions):
    def inting(x):
        return int(x)

    int_list_new = list(map(inting, int_list))
    results = {}
    for i in functions:
        results[i.__name__] = i(int_list_new)
        results[i.__name__] = i(int_list_new)
        results[i.__name__] = i(int_list_new)
        results[i.__name__] = i(int_list_new)
        results[i.__name__] = i(int_list_new)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
