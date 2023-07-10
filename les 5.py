def sort_even_odd(numbers):
    n = []
    k = []

    for num in numbers:
        if num % 2 == 0:
            n.append(num)
        else:
            k.append(num)


    sorted_numbers = n + k
    return sorted_numbers


print(sort_even_odd([3,1,4,5,6,7,8,9,3,13,14,15]))