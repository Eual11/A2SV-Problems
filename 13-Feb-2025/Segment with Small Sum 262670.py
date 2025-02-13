# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())

arr = list(map(int, input().split()))

l =0
seg_len =0
seg_sum =0
for r in range(n):
    while seg_sum+arr[r] > s:
        seg_sum-=arr[l]
        l+=1
    seg_sum+=arr[r]
    seg_len = max(seg_len, r-l+1)



print(seg_len)
