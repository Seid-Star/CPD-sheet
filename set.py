a=int(input())
b=input().strip().lower()
c=len(set(b))
if c<26:
    print("NO")
else:
    print("YES")
