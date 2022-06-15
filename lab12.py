f = open("quotes.txt", "r")

sen = f.read().lower().strip().split(' ')

words = len(sen)

print('number of words = ', words)