# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter
n, k = map(int, input().split())
arr = list((map(int, input().split())))

c = Counter()

res =[0,0]
max_len =0
left =0
for right in range(n):
    c[arr[right]] +=1

    while len(c) >k:
        c[arr[left]]-=1
        if(c[arr[left]]==0):
            del c[arr[left]]
        left+=1

    if right-left+1 > max_len:
        max_len = right-left+1
        res = [left+1, right+1]

print(*res)
