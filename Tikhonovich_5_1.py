def find_numbers(N, M, K):
    count = 0
    number = K + 1

    while count < N:
        if number % M == 0:
            print(number)
            count += 1
        number += 1

N = 10  # Количество чисел, которые нужно найти
M = 5   # Кратное число
K = 20  # Начальное значение (искать числа больше K)

find_numbers(N, M, K)