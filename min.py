l = [1, 12, 10, 13]
minimum = maximum = l[0]

for i in l:
    if i < minimum:
        minimum = i
    elif i > maximum:
        maximum = i

print("Minimum value:", minimum)
print("Maximum value:", maximum)
