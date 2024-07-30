count=0
with open("count.txt","r")as f:
    data=f.read()
    print(data)

    numbers=data.split(",")
    for value in numbers:
        if(int(value)%2==0):
            count+=1
print(count)



