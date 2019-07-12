name = input('Enter your name: ')
print('Hello, ', name)

number_1 = input('Enter x: ')
number_2 = input('Enter y: ')

print(number_1, '+', number_2, '=', float(number_1) + float(number_2))

password = 'qwerty'

while True:
    message = input('Enter password: ')
    if message == password:
        print('Welcome!')
        break
    else:
        print('Your password is wrong. Please, enter again.')

mylist = []

while True:
    msg = input('Enter new item or "STOP" to finish: ')
    if msg.lower() == 'stop':
        break

    mylist.append(msg)

print(mylist)
