n = int(input("Enter the no of elements: "))
l = []
for i in range(n):
    l.append(int(input()))
s = int(input("Enter sum value: "))
count = 0
for i in range(n):
    for j in range(n):
        if (l[i]+l[j])%s==0 and i<j:
            count += 1
print(count)
