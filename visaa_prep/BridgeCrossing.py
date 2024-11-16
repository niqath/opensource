X,Y,Z = map(int,input().split())
if Y>=Z:
    max_mangoes=0
else:
    max_mangoes=(Z-Y)//X
print(max_mangoes)
