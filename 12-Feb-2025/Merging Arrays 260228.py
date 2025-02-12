# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))



merged =[0]*(n+m)

l1, l2 =0,0

while l1 < n or l2 < m:

    if(l2==m or (l1 < n and a[l1] < b[l2]) ):
        merged[l1+l2] = a[l1]
        l1+=1
    else:
        merged[l1+l2] = b[l2]
        l2+=1


for c in merged:
    print(c, end=" ")
