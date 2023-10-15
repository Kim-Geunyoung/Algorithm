'''
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
'''

# 풀이 26
def solution(s, n):
    l_lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = []
    for i in s:
        if i == ' ':
            answer.append(' ')
        elif i.islower():
            temp = s_lst.index(i)
            temp = 25 - temp
            if temp <= n:
                answer.append(s_lst[n-temp-1])
            elif temp > n:
                answer.append(s_lst[s_lst.index(i)+n])
        elif i.islower()==False:
            temp = l_lst.index(i)
            temp = 25 - temp
            if temp <= n:
                answer.append(l_lst[n-temp-1])
            elif temp > n:
                answer.append(l_lst[l_lst.index(i)+n])
    return ''.join(answer)

print(solution('AB', 1))

# s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))

# (ord(s[i])-ord('A')+ n)

# 24 - 1 + 4
# 27

# 27%26 + 1
# 2