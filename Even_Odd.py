a,b=map(int,input().split())
arr=[]
if a%2==0:
    c=a//2
else:
    c=(a+1)//2
if c>=b:
    b=b-1
    d=(b*2)+1
    print(d)
else:
    print(2*(b-c))
