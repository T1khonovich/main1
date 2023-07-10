import collections

l = list('hello')
print(l)
words = ['hello', 'python', 'world']
print (words[1][2])

words[1] = 'pycharm'
print(words)

numbers = [i*2 for i in range (10)]
print(numbers)

from collections import *

start = int(input())
stop = int(input())
step = int(input())

from collections import Counter

numbers = [i for i in range (start, stop, step)]

text = input().lower().split()
