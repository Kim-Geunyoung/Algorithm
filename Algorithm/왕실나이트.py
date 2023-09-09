'''
입력조건 :
첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력문자는 a1처럼 열과 행으로 이뤄진다.

출력조건 :
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력
'''

# 풀이
import sys
input = sys.stdin.readline
temp = input()
count = 0
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = lst.index(temp[0])+1
y = int(temp[1])
dx = 0
dy = 0
step = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]
for i in step:
    dx = x + i[1]
    dy = y + i[0]
    
    if dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8:
        count += 1
print(count)