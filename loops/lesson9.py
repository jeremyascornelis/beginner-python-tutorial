#Nested loops

x = ["big", "small", "light", "heavy"]
y = ["iron", "silver", "platinum", "diamond"]

a = 0
b = 0

for i in x:
    for j in y:
        print(x[a], y[b])
        b += 1
    print("\n")
    a += 1
    b = 0