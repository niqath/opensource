def dnd(n,m,a):
    sum_divisible=0
    sum_not_divisible=0
    
    for num in a:
        if num % m == 0:
            sum_divisible += num
        else:
            sum_not_divisible += num
    return sum_divisible-sum_not_divisible

n,m = map(int,input().split())
a=list(map(int,input().split()))
print(dnd(n,m,a))
