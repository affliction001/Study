enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudilo',
    'image': ['img1.jpg', 'img2.jpg', 'img3.jpg'],
}

print('\n***** Example 1 *****')

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy)

for ene in all_enemies:
    print(ene)

print('\n***** Example 2 *****')

counter = 0
while counter < len(all_enemies):
    if counter % 2 == 0:
        all_enemies[counter]['health'] = all_enemies[counter]['health'] - counter * 3
    counter += 1

for ene in all_enemies:
    print(ene)

print('\n***** Example 3 *****')

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

counter = 0
while counter < len(all_enemies):
    if counter % 2 == 0:
        all_enemies[counter]['health'] = 'DEAD'

    counter += 1

for ene in all_enemies:
    print(ene)

print('\n***** END *****')
