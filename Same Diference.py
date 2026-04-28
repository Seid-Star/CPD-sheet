from collections import defaultdict
a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    freq=defaultdict(int)
    count=0 
    for i in range(b):
        c=arr[i]-i
        count+=freq[c]
        freq[c]+=1  
    print(count)
