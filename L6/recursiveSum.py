#print sum by using recursion
n=int(input("n="))
def recursive_sum(x):
    if x==0:
        return 0
    return recursive_sum(x-1)+x
sum=recursive_sum(n)
print(sum)        
