# Problem: Sum - https://codeforces.com/contest/1742/problem/A

n = int(input())

res =[]

for _ in range(n):
    l = list(map(int, input().split()))

    if(sum(l)/2 in l):
        res.append("YES")
    else:
        res.append("NO")


for c in res:
    print(c)