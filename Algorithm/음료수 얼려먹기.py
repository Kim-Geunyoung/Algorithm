import sys
from collections import deque

def dfs(i, k):
    if i <= -1 or i >= n or k <= -1 or k >= m:
        return 0
    if case[i][k] == 0:
        case[i][k] = 1
        dfs(i, k+1)
        dfs(i, k-1)
        dfs(i+1, k)
        dfs(i-1, k)
        return 1
    return 0

input = sys.stdin.readline
n, m = map(int, input().split())
case = []
count = 0
for k in range(n):
    temp = str(input())
    temp_lst = []
    for i in range(len(temp)-1):
        temp_lst.append(int(temp[i]))
    case.append(temp_lst)


for i in range(n):
    for k in range(m):
        if dfs(i, k) == 1:
            count += 1
            
print(count)