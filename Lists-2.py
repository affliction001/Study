cars = ['BMW', 'Mersedes', 'Audi', 'Lamborgini', 'Tesla']

print('\t*** Example 1 ***')
my_str = ''
for car in cars:
    my_str += car + ' '
print(my_str)

print('\n\t*** Example 2 ***')
number_list = list(range(0, 10))
for x in number_list:
    number_list[x] = x * 2
print(number_list)
number_list.sort(reverse=True)
print(number_list)

print('\n\t*** Example 3 ***')
print('Max number is: ' + str(max(number_list)))
print('Min number is: ' + str(min(number_list)))
print('Sum of list\'s numbers is: ' + str(sum(number_list)))

print('\n\t*** Example 4 ***')
bit_of_cars = cars[1:4]
print(bit_of_cars)

bit_of_cars = cars[:3]
print(bit_of_cars)
bit_of_cars = cars[0:3]
print(bit_of_cars)

bit_of_cars = cars[2:]
print(bit_of_cars)
bit_of_cars = cars[-3:]
print(bit_of_cars)

bit_of_cars = cars[-4:-1]
print(bit_of_cars)

print('\n\t*** Example 5 ***')
new_car = 'Aston Martin'
# how to copy list
new_cars = cars  # wrong!!! copied a pointer for the list
cars.append(new_car)
print(new_cars)
print(cars)

new_cars = cars[:]  # right!!! created a new list with same elements
cars.remove(new_car)
print(new_cars)
print(cars)
