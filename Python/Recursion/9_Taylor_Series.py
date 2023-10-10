p = 1
f = 1
def e(x, n):
    global p, f                 # This is the way you can declare static variable in python so that we can modify the way we want in the function
    if(n == 0):                 # Static variable: Once the variable is declared then it will never takes its original value is a static function 
        return 1
    else:
        r = e(x, n-1)
        p = p * x
        print(p)
        f = f * n
        print(f)
        return r + p/f
    

# print(e(4,10))

# def e(x, n, p=1, f=1):
#     # print(p)
#     # print(f)
#     if n == 0:
#         return 1
#     else:
#         r = e(x, n-1, p, f)
#         p *= x
#         print(p)
#         f *= n
#         print(f)
#         return r + p / f
# print(e(4, 10))

s = 1                       
def e(x, n):
    global s              # the variable is getting modified because of global keywork 
    if (n == 0):
        return s
    s = 1 + x/n * s
    return e(x, n-1)

print(e(4, 10))
