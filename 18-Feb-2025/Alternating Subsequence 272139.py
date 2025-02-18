# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def solve(arr):

    seq =[arr[0]]

    for i in range(1, len(arr)):
        top = seq[-1]
        n = arr[i]
        if(n <0 and top<0):
            # both negative, maximize by taking the max of the two
            seq.pop()
            seq.append(max(n, top))
        elif(n >0 and top>0 ):
            # both posetive, maximize by taking the max of the two
            seq.pop()
            seq.append(max(n, top))
        else:
            seq.append(n)
        


    return sum(seq)


t = int(input())

res =[]


for _ in range(t):
    _ = input()

    arr = list(map(int, input().split()))
    res.append(solve(arr))


for c in res:
    print(c)
