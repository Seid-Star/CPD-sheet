a=int(input())
freq={}
for x in range(a):
    b=input().strip()
    if b not in freq:
        print("OK")
        freq[b]=1
    else:
        print(b+str(freq[b]))
        freq[b]+=1
    
