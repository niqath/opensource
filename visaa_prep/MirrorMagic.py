N=int(input())
mtrx=[]
for i in range(N):
    r = list(map(int,input().split()))
    mtrx.append(r)
mirror_magic = [r[::-1] for r in mtrx]
for r in mirror_magic:
    print(" ".join(map(str, r)))
