N = int(input())
def mul_chal(l,d): #L=LIMIT and D= DIVISOR
    return l//d
c3 = mul_chal(N,3) #NO OF MULTIPLES OF 3
c5 = mul_chal(N,5)  #NO OF MULTIPLES OF 5
cb = mul_chal(N,15) #NO OF MULTIPLES OF BOTH
r = c3+c5-cb
print(r)
