cities = [
    'New York',
    'Moscow',
    'Ottawa',
    'Kyoto',
    'Seul'
]

print('*** Example 1 ***')
print(cities)
print(len(cities))
print(cities[0])

print('*** Example 2 ***')
i = 0
while i < len(cities):
    print(cities[i])
    i += 1

print('*** Example 3 ***')
cities.append('Tokyo')  # добавляет элемент в конец списка
cities.append('Pusan')
print(cities)

print('*** Example 4 ***')
cities.insert(5, 'Verona')  # добавляет элемент в любое место списка по индексу,
# остальные элементы сдвигаются вправо.
print(cities)

print('*** Example 5 ***')
del cities[1]  # удаляет элемент списка по индексу
print(cities)

cities.remove('Ottawa')  # удаляет элемент списка по содержанию
print(cities)

deleted_city = cities.pop(0)  # удаляет элемент из списка и возвращает удаленный элемент
print('Deleted city is: ' + deleted_city)
print(cities)

print('*** Example 6 ***')
cities.reverse()  # переворачивает список наоборот
print(cities)

print('*** Example 7 ***')
cities.sort()  # сортирует список по алфавиту
print(cities)
cities.sort(reverse=True)  # сортирует список по алфавиту в обратном порядке
print(cities)
