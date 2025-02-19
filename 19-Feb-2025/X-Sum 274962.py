# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def max_bishop_attack(n, m, board):
    main_diag = {}  
    anti_diag = {}  


    for i in range(n):
        for j in range(m):
            main_diag[i - j] = main_diag.get(i - j, 0) + board[i][j]
            anti_diag[i + j] = anti_diag.get(i + j, 0) + board[i][j]

    max_sum = 0

    for i in range(n):
        for j in range(m):
            bishop_sum = main_diag[i - j] + anti_diag[i + j] - board[i][j]
            max_sum = max(max_sum, bishop_sum)

    return max_sum


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(max_bishop_attack(n, m, board))
