a=[1,4,5,2,3,8]
b=a[0]
c=a[0]

for i in a:
    if i>b:
        b=i
    elif i<c:
        c=i
print("lar",b)
print("small",c)            
 