a=input().strip()
arr=[0]*len(a)
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        arr[i+1]=1
for j in range(1,len(arr)):
    arr[j]+=arr[j-1]
b=int(input())
for x in range(b):
    c,d=map(int,input().split())
    print(arr[d-1]-arr[c-1])
