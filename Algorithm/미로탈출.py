import sys
from collections import deque

input = sys.stdin.readline

def move(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if lst[nx][ny]==0:
                continue
            
            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                queue.append((nx, ny))
    return lst[n-1][m-1]


n, m = map(int, input().split())
answer = []
lst = []
for i in range(n):
    # temp = input().strip()
    # temp_lst = []
    # for k in range(m-1):
    #     temp_lst.append(int(temp[k]))
    # lst.append(temp_lst)
    lst.append(list(map(int, input().strip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
print(lst)
print(move(0, 0))