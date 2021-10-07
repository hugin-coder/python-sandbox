def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)


def print_if(test_func, numbers):
    for n in numbers:
        if test_func(n):
            print(n)

def test_even(n):
    return n % 2 == 0


#print(factorial(950))
print_if(lambda n: n % 4 == 0, [2, 13, 4, 23, 6, 45])
print_if(test_even, [2, 13, 4, 23, 6, 45])
