# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

n = int(input())

res =[0, 0, 0]


for _ in range(n):
    x, y, z = map(int, input().split())
    res[0]+=x
    res[1]+=y
    res[2]+=z


if(res ==[0,0,0]):
    print("YES")
else:
    print("NO")