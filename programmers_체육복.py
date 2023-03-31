def solution(n, lost, reserve):
    ori = [1]*n
    for l in lost:
        ori[l-1] -= 1
        
    for k in reserve:
        ori[k-1] += 1
   
    for i in range(n):
        if ori[i] ==0:
            if i>0 and ori[i-1] == 2:
                ori[i-1] -= 1
                ori[i] += 1
            elif i < n-1 and ori[i+1] == 2:
                ori[i+1] -= 1
                ori[i] += 1
                
    sum = 0
    for j in ori:
        if j > 0:
            sum += 1
    return sum
            

            
print(solution(5, [2,4], [1,3,5]))