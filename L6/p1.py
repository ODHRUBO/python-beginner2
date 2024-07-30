cities=["dhaka","chittagong","rajshahi","khulna","borishal","sylhet"]
heros=["thor","ironman","superman","captain america"]
def print_len(list):
    print(len(list))

#print list length
print_len(cities)
print_len(heros)

#print list in one line
def print_list(list):
    for item in list:
        print(item,end=" ")
    
print_list(cities)
print()
print_list(heros)   