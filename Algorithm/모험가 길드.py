import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
count = 0
temp = 0
e_p = 1
for i in range(len(lst)):
    temp += 1
    if e_p < lst[i]:
        e_p = lst[i]
    if temp >= e_p:
        count += 1
        e_p = 1
        temp = 0
print(count)