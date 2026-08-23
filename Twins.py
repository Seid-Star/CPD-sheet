a=int(input())
arr=list(map(int,input().split()))
arr.sort()
brr=[]
count=0
while sum(brr)<=sum(arr):
    brr.append(arr[-1])
    arr.pop()
    count+=1
print(count)
