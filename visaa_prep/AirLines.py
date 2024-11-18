X,N = map(int,input().split())
existing_capacity = X*100
remaining_passengers = max(0, N-existing_capacity)
additional_planes=(remaining_passengers + 99)//100
print(additional_planes)
