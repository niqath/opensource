X,Y,Z = map(int,input().split())
total_min = X*Y
no_of_min_in_z_days= Z*1440
if total_min<=no_of_min_in_z_days:
    print("YES")
else:
    print("NO")
