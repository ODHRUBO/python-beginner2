#print 1 to n backwords using recursion
m=int(input("number? "))
def show(n):
    if(n==0):#base case
        return
    print(n)
    show(n-1)
show(m)