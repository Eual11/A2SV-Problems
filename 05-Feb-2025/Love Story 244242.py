# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

def solve(s:str)->int:
    t ="codeforces"
    return sum([1 if s[i]!=t[i] else 0 for i in range(len(s))])


n = int(input())
res =[]
for i in range(n):
    s = input()
    res.append((solve(s)))

for c in res:
    print(c)