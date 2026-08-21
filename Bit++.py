a=int(input())
count=0
for x in range(a):
    b=input().strip()
    if '+' in b:
        count+=1
    else:
        count-=1
print(count)
