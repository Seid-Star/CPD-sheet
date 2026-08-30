a=int(input())
arr=[]
for x in range(a):
    b,c=map(int,input().split())
    arr.append([b,c])
arr.sort()
for i in range(1,a):
    if arr[i][1]<arr[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
