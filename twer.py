text = input ('enter text:')
first_space = text.find(' ')
second_space = text.rfind(' ')
center = text[first_space: second_space +1]
second_word = text[second_space +1]
word = second_word + center + first_space
print(word)