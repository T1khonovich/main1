age = 34
name = 'Alex'
is_human = 'True'

# text = 'Hello your age is human '
text1 = 'Hello' + name + ' your age ' + str(age) + 'is human ' + str(is_human)
#text2 = 'Hello %s your age %d is human %d' % (name, age, is_human)
text3 = 'Hello {} your age {} is human {}'.format(name, age, is_human)
text4=  f'Hello {name} your age {age * 2} is human {is_human}'
print(text1)
#print(text2)
print(text3)
print(text4)
print('\N{popcorn}') #в выводе будет смайлик искать название в UNICODE
text = 'Hello world python'
print(text.split()) #['Hello', 'world', 'python'] 