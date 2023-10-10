# def fib(n):
#     if (n <= 1):
#         return n
#     return fib(n-2) + fib(n-1)

# for i in range(1,10):
#     print(fib(i))


F = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  # this is Memoization

def fib(n):
    if (n<=1):
        F[n] = n
        return n
    else:
        if (F[n-2]==-1):
            F[n-2]=fib(n-2)
        if (F[n-1]==-1):
            F[n-1]=fib(n-1)
        return F[n-2] + F[n-1]

for i in range(1,10):
    print(fib(i)) 
# print(fib(8))