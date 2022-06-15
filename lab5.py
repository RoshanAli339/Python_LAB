m = input("Enter name of month: ")
y = int(input("Enter the year: "))

months = {"January":31,"February":29,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}

if ((y % 4 == 0 and y % 100 != 0) or y%400 == 0) and m == "February":
    print("30 days")
else:
    print(months[m]," days")
    