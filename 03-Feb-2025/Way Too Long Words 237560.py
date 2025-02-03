# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())

res =[]

for _ in range(n):
    word = input()

    if(len(word) <=10):
        res.append(word)
    else:
        res.append("".join([word[0],str(len(word)-2), word[-1]]))


for c in res:
    print(c)