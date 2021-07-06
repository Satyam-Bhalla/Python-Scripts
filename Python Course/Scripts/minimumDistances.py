n = int(input())
l = list(map(int,input().split()))
mind = []
for i in range(len(l)):
    for j in range(i):
        if l[i]==l[j]:
            mind.append(abs(i-j))
if len(mind)==0:
    print(-1)
else:
    print(min(mind))
