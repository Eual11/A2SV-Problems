# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B



#for while combo


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res =[0]*m

i=0
for j in range(len(b)):

    while i < len(a) and a[i] < b[j]:
        i+=1

    res[j]=i

for c in res:
    print(c, end= " ")
