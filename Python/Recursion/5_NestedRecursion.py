def fun(n):

    if n > 100:
        return n-10
    return fun(fun(n+11))

print(fun(95))