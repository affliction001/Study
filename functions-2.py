def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address,
    }

    return record


def give_award(medal, *persons):
    """Give Medals to Persons"""
    for person in persons:
        print(person.title() + ' recived medal!')


print('\n***** Example 1 *****')

user1 = create_record('Vasya', 777, 'Teasdgwads')
user2 = create_record('Ykrnrg', 333, 'Teasdgwads')
user3 = create_record('jIIEgsg', 222, 'Teasdgwads')
user4 = create_record('Ytwe', 555, 'Teasdgwads')

print(user1)
print(user2)
print(user3)
print(user4)

print('\n***** Example 2 *****')

give_award('Za hz', 'Vasya', 'Petya', 'Alexandr', 'Mudilo')
