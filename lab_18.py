def isPalindrome(a):
    l = len(a)
    s=''
    for i in range(l-1, -1, -1):
        s += a[i]
    if s == a: return True
    else: return False


a = input("Enter a string: ")
if isPalindrome(a):
    print(a, " is a Palindrome")
else:
    print(a, " is not a Palindrome")
    