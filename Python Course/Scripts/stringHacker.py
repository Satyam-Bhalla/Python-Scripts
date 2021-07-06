l = list(input())
n = []
sum = 0
for i in range(len(l)):
    if (l[i]).isdigit() :
        n.append(l[i])
    else :
        if len(n)!=0:
            s= "".join(n)
            sum+=int(s)
            n.clear()



            
if len(n) > 0:
   s= "".join(n)
    sum += int(s)
    n.clear()

temp =0
while len(list(str(sum))) != 1:
    while sum != 0:
        temp += sum%10
        sum = int(sum/10)
    sum = temp
    temp =0
print(sum)






