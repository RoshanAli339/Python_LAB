f = open("quotes.txt", "r")

#converting all letters to lowercase for easy comparison
sen = f.read().lower().strip().split(' ')

words = len(sen)

print('number of words = ', words)