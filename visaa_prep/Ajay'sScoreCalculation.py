T=int(input())
for i in range(T):
    X,N = map(int,input().split())
    score_per_testcase = X//10
    score = score_per_testcase*N
    print(score)
