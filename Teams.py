a=int(input())
count=0
for x in range(a):
    b,c,d=map(int,input().split())
    if b+c+d>=2:
        count+=1
print(count)
