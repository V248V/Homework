def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result / 2) + 1):
            if result % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result

    return wrapper


@is_prime
def sum_three(first, second, third):
    result = first + second + third
    return result


result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 3, 6)
print(result)
