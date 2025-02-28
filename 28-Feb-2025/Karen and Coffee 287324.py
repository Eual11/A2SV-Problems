# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from itertools import accumulate
MAX = 200000

D = [0]*(MAX+2)


n, k, q = map(int, input().split())


for _ in range(n):
    l, r = map(int,input().split())

    D[l]+=1
    D[r+1]-=1

    
D = list(accumulate(D))

D =[1 if n>=k else 0 for n in D]
D = list(accumulate(D))
res =[]
for _ in range(q):
    a, b = map(int, input().split())
    res.append(D[b]-D[a-1])


for c in res:
    print(c)
