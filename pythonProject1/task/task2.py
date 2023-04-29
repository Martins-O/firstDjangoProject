def is_divisible(num, *args):
    for number in args:
        if number % num != 0:
            return False
    return True


def find_factors(*args):
    factors = []
    lowest_number = min(args)
    aim = min(args)
    i = 2
    while True:
        if i == aim:
            break
        if is_divisible(i, *args) is False:
            i += 1
            continue
        if lowest_number % i != 0:
            i += 1
            continue
        factors.append(i)
        lowest_number /= i
        if lowest_number == 1:
            break
    return factors
