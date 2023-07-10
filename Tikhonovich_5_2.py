def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль!"

def calculator():
    print("Добро пожаловать в калькулятор!")
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operator = input("Введите действие (+, -, *, /) или 'q' для выхода: ")

            if operator == 'q':
                print("Калькулятор закрыт.")
                break

            num2 = float(input("Введите второе число: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Недопустимое действие. Попробуйте снова.")
                continue

            print("Результат:", result)

        except ValueError:
            print("Ошибка: введите корректное число.")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")

calculator()