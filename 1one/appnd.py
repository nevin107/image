a=[23,23,4,4,5,6,7,7,8]
b=[]

for i in a:
    if i not in b:
        b.append(i)
print("value",b)        