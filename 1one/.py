a=[12, 4, 3, 4, 6, 7, 100, 18, 2, 18, 18]
b=[]


for i in a:
    if i not in b:
        b.append(i)
        
print("list:",b) 
global       