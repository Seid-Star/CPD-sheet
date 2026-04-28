a=int(input())
freq={}
arr=[]
for x in range(a):
    b,c=map(str,input().split())
    arr.append((b,c))
    if b not in freq:
        freq[b]=int(c)
    else:
        freq[b]+=int(c)
d=max(freq.values())
brr={}
for i,j in arr:
    j=int(j)
    if i not in brr:
        brr[i]=j
    else:
        brr[i]+=j
    if brr[i]>=d and freq[i]==d:
        print(i)
        break

