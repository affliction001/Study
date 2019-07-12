def print_hello(name):
    """function diescription"""
    print('Hello, ', name, '!')


def summ(x, y):
    print(x + y)


def get_summ(x, y):
    return x + y


def factorial(x):
    """Calculate Factorial of number x"""
    counter = 1
    result = 1
    while counter <= x:
        result *= counter
        counter += 1

    return result


# ****************** Main ********************
print('\n***** Example 1 *****')
# user = input('Enter your name: ')
# print_hello(user)

print('\n***** Example 2 *****')
summ(10, 20)

print('\n***** Example 3 *****')
x = get_summ(33, 22)
print(x)

print('\n***** Example 4 *****')
for i in range(1, 11):
    print(i, '! = ', factorial(i), sep='')

