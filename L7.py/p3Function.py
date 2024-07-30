#find a word learning in  a file using function
def check_of_word(word):
    
    with open ("practice.txt","r")as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
            print("not found")
check_of_word("java")