a=int(input())
for x in range(a):
    b=input().strip()
    b=b.replace('p','1')
    b=b.replace('q','p')
    b=b.replace('1','q')
    print(b[::-1])
