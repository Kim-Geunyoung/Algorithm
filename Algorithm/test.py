# def solution(dice):
#     from itertools import combinations
#     n = len(dice)
#     dice_lst = []

#     for i in range(n):
#         dice_lst.append(i)

#     combi = list(combinations(dice_lst, n//2))

#     answer = []

#     # [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
#     for i in range(len(combi)):
#         count = 0
#         temp = dice[combi[i][0]]
#         for k in range(1, n//2):
#             new_temp = []
#             for x in dice[k]:
#                 for y in temp:
#                     new_temp.append(x+y)
#             temp = new_temp

#         combi_b = dice_lst
#         for j in range(n//2):
#             combi_b.remove(combi[i][j])
        
#         temp_b = dice[combi_b[0]]
#         for kk in range(1, n//2):
#             new_temp_b = []
#             for xx in dice[kk]:
#                 for yy in temp_b:
#                     new_temp_b.append(xx+yy)
#             temp_b = new_temp_b
        
#         for z in range(len(temp)):
#             for zz in range(len(temp_b)):
#                 if temp[z] > temp_b[zz]:
#                     count += 1
                    
#         answer.append(count)
    
#     return answer.index(max(answer))

# solution([[1,2,3,4,5,6], [2,2,4,4,6,6]])
lo = range(15)
lp = range(10)
lo_lp = list()

for i in range(len(lp)):
    lo_lp.append(lo[i] + lp[i])
print(lo_lp)

