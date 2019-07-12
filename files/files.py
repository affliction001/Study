import datetime


inputfile = 'textfile.txt'
inputpasswords = 'passwords.txt'
outputpasswords = 'outpasswords.txt'
logfile = 'log.txt'

# mode='r - read; w = write; a = append; r+ = read and write'
log = open(logfile, mode='w', encoding='utf-8')
log.write(str(datetime.datetime.now())[:-7] + '\n\n')
log.close()

print('\n***** Example 1 *****')

myfile = open(inputfile, mode='r', encoding='utf-8')

file_content = myfile.read()
print(file_content)

myfile.close()

log = open(logfile, mode='a', encoding='utf-8')
log.write('>>> Example 1 is finished successfully.\n')
log.close()

print('\n***** Example 2 *****')
myfile = open(inputfile, mode='r', encoding='utf-8')

for num, line in enumerate(myfile, start=1):
    print(num, '\t', line.strip())

myfile.close()

log = open(logfile, mode='a', encoding='utf-8')
log.write('>>> Example 2 is finished successfully.\n')
log.close()

print('\n***** Example 3 *****')

passwords = open(inputpasswords, mode='r', encoding='utf-8')

magic_word = 'ass'

for password in passwords:
   if magic_word in password:
       print(password.strip())

passwords.close()

log = open(logfile, mode='a', encoding='utf-8')
log.write('>>> Example 3 is finished successfully.\n')
log.close()

print('\n***** Example 4 *****')

passwords = open(inputpasswords, mode='r', encoding='utf-8')
outpass = open(outputpasswords, mode='w', encoding='utf-8')

magic_word = 'war'
counter = 1

for password in passwords:
    if magic_word in password:
        outpass.write(str(counter) + ': ' + password)
        counter += 1
        print('"', password.strip(), '"', ' is writed.', sep='')

passwords.close()
outpass.close()

log = open(logfile, mode='a', encoding='utf-8')
log.write('>>> Example 4 is finished successfully.\n')
log.close()
