# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())


problems =0

for _ in range(n):
    sure=sum(list(map(int, input().split())))
    problems+= int(sure>=2)

print(problems)