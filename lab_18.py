def isPalindrome(a):
    s = a[: : -1]
    if s.lower() == a.lower(): return True
    else: return False


a = input("Enter a string: ")
if isPalindrome(a):
    print(a, " is a Palindrome")
else:
    print(a, " is not a Palindrome")
    