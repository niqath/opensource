N=int(input())
arr = list(map(int, input().split()))
unique_ele = []
s=set()
for num in arr:
    if num not in s:
        unique_ele.append(num)
        s.add(num)
print(" ".join(map(str, unique_ele)))
