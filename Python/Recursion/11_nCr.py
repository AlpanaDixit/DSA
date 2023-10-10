def C(n, r):
    if (r==0 or n==r):
        return 1
    else:
        return C(n-1, r-1) + C(n-1,r)
    
print(C(5,2))