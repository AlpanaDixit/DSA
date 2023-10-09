def Fact(n):

    if (n < 0):
        return "Number must be positive"
    elif (n==0):
        return 1
    else:
        return Fact(n-1) * n

print(Fact(10))
