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
    #standard deviation is the square root of variance
    return variance(a,n)**(1/2)

a=[]
ele = input("Enter the elements: ")
a = ele.split(' ')
a = [int(x) for x in a]
n = len(a)
print("Mean of given data: ", mean(a,n))
print("Variance of given data: ", variance(a,n))
print("Standard deviation of given data: ", sd(a,n))
