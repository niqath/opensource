def bestCoupon(x):
    d1=x*0.10
    d2=100
    maxD=max(d1,d2)
    finalAmount=x-maxD
    return int(finalAmount)
    
x=int(input())
print(bestCoupon(x))
