st=input().strip()
res=""
char_count=st[0]
count=0
for char in st:
    if char == char_count:
        count += 1
    else:
        res += char_count+str(count)
        char_count = char
        count = 1
res += char_count + str(count)
print(res)

