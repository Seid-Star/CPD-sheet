a=int(input())
arr=list(map(int,input().split()))
b=arr.count(4)
three=arr.count(3)
two=arr.count(2)
one=arr.count(1)
if one>three:
    one-=three
    b+=three
else:
    three-=one
    b+=one
    b+=three
    one=0
b+=two//2
if two%2==1:
    b+=1
    one-=min(one,2)
if one>0:
    b+=(one+3)//4
print(b)
