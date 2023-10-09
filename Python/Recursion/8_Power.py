def Pow(m, n):
    if (n == 0):
        return 1
    else:
        return Pow(m, n-1) * m
    
print(Pow(10, 2))


################ Another method ##############

def Pow1(m, n):
    if (n == 0):
        return 1
    
    if (n % 2 == 0):
        return Pow1(m * m, n/2) 
    else:
        return m * Pow1(m * m, (n-1)/2)
    
print(Pow1(10,2))