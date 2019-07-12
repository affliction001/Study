enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}

print(enemy)

print('\n***** Example 1 *****')

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("Name = " + enemy['name'])

print('\n***** Example 2 *****')

enemy['rank'] = 'Admiral'
print(enemy)

print('\n***** Example 3 *****')

del enemy['rank']
print(enemy)

print('\n***** Example 4 *****')

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30

if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print('\n***** Example 5 *****')

print(enemy.keys())
print(enemy.values())
