# Problem: Books - https://codeforces.com/contest/279/problem/B

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_len =0
left =0
seg_sum =0
for right in range(n):

    seg_sum+=arr[right]
    while seg_sum > k:

        seg_sum-=arr[left]
        left+=1
    max_len = max(max_len, right-left+1)


print(max_len)
