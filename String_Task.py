a=list(input().lower())
b='aeiouy'
c=''
for i in range(len(a)):
    if a[i] not in b:
        c+='.'+a[i]
print(c)
