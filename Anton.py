    a=int(input())
    b=input().strip()
    c=b.count('A')
    d=b.count('D')
    if c>d:
        print("Anton")
    elif c<d:
        print("Danik")
    else:
        print("Friendship")
