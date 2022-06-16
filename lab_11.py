words = 0
digits = 0
upper = 0
lower = 0

s = input("Enter a sentence: ")
#to define the end of the sentence
s = s.strip() + '.'

for i in s:
    if i == ' ' or i == '.':
        words += 1
    if i.isdigit():
        digits += 1
    elif i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

print('Number of words: ', words)
print('Number of digits: ', digits)
print('Number of lowercase letters: ', lower)
print('Number of uppercase letters: ', upper)
