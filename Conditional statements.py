print('\t*** Example 1 ***')
x = 10

if x == 10:
    print('x is equal 10')
elif x > 20:
    print('x is too much')
else:
    print('x is undefined')


print('\n\t*** Example 2 ***')
lst = list(range(0, 10))
x = 5
if x in lst:
    print('Yes, 5 is in the list')
else:
    print('5 is not in the list')

print('\n\t*** Example 3 ***')
cars = ['BMW', 'KIA', 'Audi', 'Genesis', 'Ford', 'Mersedes', 'Toyota', 'Volks Wagen', 'Dodge']
german_cars = ['BMW', 'Audi', 'Mersedes', 'Volks Wagen']

for car in cars:
    if car in german_cars:
        print(car + ' is Germany car.')
    else:
        print(car + ' is not Germany car.')

print('\t*** End ***')