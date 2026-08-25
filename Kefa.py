a=int(input())
arr=list(map(int,input().split()))
count=1
Max=0
for i in range(1,a):
    if arr[i-1]<=arr[i]:
        count+=1
    else:
        if Max<=count:
            Max=count
        count=1
if count>=Max:
    Max=count
print(Max)
    
