def check_if_numbers_are_divisible(num, *args):
    for number in args:
        if number % num != 0:
            return False
    return True


def find_factors_of_numbers(*args):
    multiples = []
    lowest = min(args)
    aim = lowest
    i = 2
    while i < aim:
        if check_if_numbers_are_divisible(i, *args) and lowest % i == 0:
            multiples.append(i)
            lowest //= i
            if lowest == 1:
                break
        else:
            i += 1
    return multiples


print(find_factors_of_numbers(1000, 100000))
