print(input().replace(' ', '-')) #1 способ

text = input()
new_text = "-".join(text.split(" "))
print(new_text)  #2 способ