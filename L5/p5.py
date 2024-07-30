numbers=(1,4,9,16,25,36,49,64,81,100)
n=int(input("what's nuumber ? "))
i=1
while i<len(numbers):
    if(numbers[i]==n):
        print("Found in index ",i)
        break
    
    else:
        print("not found")
    i+=1

    
