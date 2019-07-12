from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.GREEN)

operator = input("Что делаем? (+,-,*,/): ")

print(Back.CYAN)

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y
else:
    result = "Выбранна неверная операция: " + operator

print(Back.YELLOW)

print('Результат: ' + str(result))
input()
