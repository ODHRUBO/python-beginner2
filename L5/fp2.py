tuple=(1,4,9,16,25,36,49,64,81,100)
n=int(input("what's n? "))

indx=0
for number in tuple:
    if number==n:
        print("number found at index ", indx)
    indx+=1