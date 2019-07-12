import sys

filename = 'exceptions/' + input('Please enter the file name: ').strip()

while True:
    try:
        file = open(filename, mode='r', encoding='utf-8')
    except Exception:
        print('Ooops, error is somewhere! :(')
        print(sys.exc_info()[1])
        filename = 'exceptions/' + input('Please enter the correct file name: ').strip()
    else:
        print(file.read())
        file.close()
        break
    finally:
        print('Finally! :)\n')


print('***** End of Program *****')
