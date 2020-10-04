
# 6! is 6 * 5 * 4 * 3 * 2 * 1
def factorial_iterative(x):
    product = 1
    for i in range(1, x + 1, 1):
        product *= i

    return(product)


# recursion

# or 6 * 5!
# or 6 * 5 * 4!
def factorial(x):
    if x in [0, 1]:
        return 1

    return x * factorial(x - 1)
