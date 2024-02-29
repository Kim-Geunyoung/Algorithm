def solution(coin, cards):
    n = len(cards)
    mycards = cards[:4]
    del cards[:4]

    count = 0
    while len(cards)==0 or len(mycards) or coin == 0:
        for i in range(len(mycards)):
            if len(cards) > 0:
                if cards[0] + mycards[i] == n:
                    coin -= 1
                    del mycards[i]
            if len(cards) > 1:
                if cards[1] + mycards[i] == n:
                    coin -= 1
                    del mycards[i]
            
            if cards[0] + cards[1] == n:
                coin -= 2
        del cards[:2]
        count += 1
    return count

            

            


            
solution(4, [3,6,7,2,1,10,5,9,8,12,11,4])