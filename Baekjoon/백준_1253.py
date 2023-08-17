'''
문제
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

출력
좋은 수의 개수를 첫 번째 줄에 출력한다.
'''

# 음수도 생각했어야 했다

# 풀이
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
count = 0

for i in range(n):
    s = 0
    e = n-1
    p = lst[i]
    while s < e:
        if lst[s] + lst[e] > p:
            e -= 1
        elif lst[s] + lst[e] < p:
            s += 1
        elif lst[s] + lst[e] == p:
            if s == i:
                s += 1
            elif e ==i:
                e -= 1
            else:
                count += 1
                break
        
print(count)