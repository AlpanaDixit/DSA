# A = [1,2,3,4,5,6]
# length = 0
# for i in A:
#     # print(i)
#     length = length + 1

# print(length)

def len(A):
    length = 0
    for i in A:
        length = length + 1
    return(length)
    

print(len([1,2,3,4]))
print(len("Bottle"))
print(len((1,2,3,4,5)))
print(len({1,2,3,4,5,6,7,8,9}))
print(len({"A":1,"B":2}))