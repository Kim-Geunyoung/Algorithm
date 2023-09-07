# import sys
# input = sys.stdin.readline
# size = int(input())
# lst = list(input().split())
# n = 1
# m = 1
# for i in range(len(lst)):
#     if lst[i] == 'R':
#         if m + 1 <= size and m + 1 > 1:
#             m += 1
#     elif lst[i] == 'L':
#         if m - 1 <= size and m - 1 > 1:
#             m -= 1
#     elif lst[i] == 'U':
#         if n + 1 <= size and n - 1 > 1:
#             n -= 1
#     elif lst[i] == 'D':
#         if n - 1 <= size and n + 1 > 1:
#             n += 1
# print(n, m)

# 다른 방법
import sys
input = sys.stdin.readline
size = int(input())
lst = list(input().split())
x = 1
y = 1
nx = 0
my = 0
move_point = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for plan in lst:
    for i in range(len(move_point)):
        if plan == move_point[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > size or ny > size:
        continue
        
    x, y = nx, ny
print(x, y)