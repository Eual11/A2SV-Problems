# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict
n = int(input())

age_dict = defaultdict(int)

for _ in range(n):
    l, r = map(int, input().split())

    age_dict[l]+=1
    age_dict[r]-=1



years = sorted(age_dict.keys())

prev = years[0]

age = 0

years_lived =defaultdict(int)
acc =0
for year in years:
    acc+=age_dict[year]
    years_lived[year] = acc

ans =(0,float('-inf'))

for year in years:
    
    if years_lived[year] > ans[1]:
        ans =(year, years_lived[year])

print(*ans)
