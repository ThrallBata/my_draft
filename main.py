def arithmetic_sequence_elements(a, d, n):
    list_progress = []
    for i in range(n):
        list_progress.append(str(a))
        a += d
    return ', '.join(list_progress)


print(arithmetic_sequence_elements(1, 2, 5))


def arithmetic_sequence_elements1(a, r, n):
    return ", ".join((str(a+r*i) for i in range(n)))


print(arithmetic_sequence_elements(1, 2, 5))


def min_price(coins):
    pass