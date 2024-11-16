def reverseInteger(n):
    negative = n<0
    if negative:
        n=-n
    reversedNum=0
    while n!=0:
        digit=n%10
        reversedNum=reversedNum*10+digit
        n//=10
    if negative:
        reversedNum=-reversedNum
    if reversedNum <-2**31 or reversedNum>2**31-1:
        return 0
    return reversedNum
n=int(input())
print(reverseInteger(n))
