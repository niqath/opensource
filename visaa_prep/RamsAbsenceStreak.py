N = int(input())
attendance = list(map(int,input().split()))
mx = 0
count = 0 
for d in attendance:
    if d==0:
        count += 1
        mx=max(mx,count)
    else:
        count = 0
print(mx)
