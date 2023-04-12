def solution(left, right):
    sum = 0
    for k in range(left, right+1):
        temp = 2
        for i in range(2, k):
            if k % i == 0:
                temp += 1
        if temp % 2 == 0:
            sum += k
        else:
            sum -= k
    return sum