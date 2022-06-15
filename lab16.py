def mean(a, n):
    mean = 0
    for i in a:
        mean += i
    mean /= n
    return mean

def variance(a, n):
    var = 0
    m = mean(a,n)
    for i in a:
        var += (i - m)**2
    var /= n-1
    return var

def sd(a, n):
    return variance(a,n)**(1/2)

a=[]
n = int(input("Number of elements: "))
print("Enter the elements: ")
for i in range(n):
    ele = int(input())
    a.append(ele)

print("Mean of given data: ", mean(a,n))
print("Variance of given data: ", variance(a,n))
print("Standard deviation of given data: ", sd(a,n))
