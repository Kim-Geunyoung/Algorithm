'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
'''

# 풀이
def solution(left, right):
    sum = 0
    for k in range(left, right+1):
        temp = 0
        for i in range(1, k+1):
            if k % i == 0:
                temp += 1
        if temp % 2 == 0:
            sum += k
        else:
            sum -= k
    return sum