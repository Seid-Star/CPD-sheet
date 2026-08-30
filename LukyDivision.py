a=int(input())
if a%4==0 or a%7==0:
    print("YES")
elif a%44==0 or a%47==0 or a%74==0 or a%77==0:
    print("YES")
elif a%444==0 or a%447==0 or a%474==0 or a%477==0:
    print("YES")
elif a%744==0 or a%747==0 or a%774==0 or a%777==0:
    print("YES")
else:
    print("NO")
