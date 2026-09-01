a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=sum(arr[:b])
d=c
e=0
l=0
r=b
while r<len(arr):
    c=c-arr[l]+arr[r]
    if c<d:
        d=c
        e=l+1
    l+=1
    r+=1
print(e+1)
