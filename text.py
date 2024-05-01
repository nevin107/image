f=open("hi.txt","r")
r=f.read()
a=0
n=0
words=1
for i in r:
    if i==" ":
        words+=1
    elif i.isalpha():
        a+=1
    elif i.isdigit():
        n+=1
        

print(words)
print(a)
print(n)  
print(words-1)
     
