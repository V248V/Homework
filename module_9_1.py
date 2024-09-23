def apply_all_func(int_list, *functions):
    def inting(x):
        return int(x)

    int_list_new = list(map(inting, int_list))
    results = {}
    for i in functions:
        if i == min:
            results[i.__name__] = min(int_list_new)
        if i == max:
            results[i.__name__] = max(int_list_new)
        if i == len:
            results[i.__name__] = len(int_list_new)
        if i == sum:
            results[i.__name__] = sum(int_list_new)
        if i == sorted:
            results[i.__name__] = sorted(int_list_new)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
