a=int(input())
Sum1=0
Sum2=0
Sum3=0
for x in range(a):
    arr=list(map(int,input().split()))
    Sum1+=arr[0]
    Sum2+=arr[1]
    Sum3+=arr[2]
if Sum1==0 and Sum2==0 and Sum3==0:
    print("YES")
else:
    print("NO")
