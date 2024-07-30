#find a word learning in  a file

word="learning"
with open ("practice.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("not found")