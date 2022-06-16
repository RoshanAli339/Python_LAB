f = open("quotes.txt", "r")
data = f.read()

data = data.split(' ')

fdata = []
for i in data:
    if i not in fdata:
        fdata.append(i)

l1 = len(data)

print("Number of words in the file: ", l1)

for i in fdata:
    l2 = data.count(i)
    print(f"The frequency of \"{i}\" is: {l2}")
