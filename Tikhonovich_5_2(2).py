num1 = float(input('Введите первое число:'))
operator = input('Введите действие (+, -, *, /):')
num2 = float(input('Введите второе число:'))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    if num1 == 0 or num2 == 0:
        print('Умножение на 0 нельзя')
    else:
        print (num1 * num2)
elif operator == '/':
    if num1 == 0 or num2 == 0:
        print('Деление на 0 нельзя')
    else:
        print (num1 / num2)




else:
    print('Недопустимое действие. Попробуйте снова.')




