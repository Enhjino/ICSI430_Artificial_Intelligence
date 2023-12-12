def sum_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

def reduce(n):
    if n > 10:
        return reduce(sum_digits(n))
    else:
        return n
def removep(lst, pred):
    result = []
    for x in lst:
        if not pred(x):
            result.append(x)
    return result


from itertools import combinations


def power_set(lst):
    subsets = [[]]
    for i in range(1, len(lst) + 1):
        subset_combinations = list(combinations(lst, i))
        subsets.extend([list(combination) for combination in subset_combinations])

    return subsets

print(power_set([1, 2, 3, 4]))

