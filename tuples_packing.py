def multiply(*args):
    product = 1

    for arg in args:
        product *= arg
    return product

print(multiply(5, 5))