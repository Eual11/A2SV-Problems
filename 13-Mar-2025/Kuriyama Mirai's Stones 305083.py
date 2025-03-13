# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from itertools import accumulate
input()

arr = list(map(int, input().split()))
t = int(input())


p_sum = list(accumulate(arr))
sorted_psum = list(accumulate(sorted(arr)))
res =[]


for _ in range(t):
    q, l, r = map(int, input().split())

    s=0
    if q==1:
        if l >1:
            s = p_sum[r-1]-p_sum[l-2]
        else:
            s = p_sum[r-1]
    else:
        if l > 1:
            s = sorted_psum[r-1]-sorted_psum[l-2]
        else:
            s = sorted_psum[r-1]
    res.append(s)



for c in res:
    print(c)
