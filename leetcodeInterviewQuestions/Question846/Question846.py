from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
            
        while len(hand)>0:    
            m=min(hand)  
            hand.remove(m)          
            for i in range(1,groupSize):
                if m+1 in hand:
                    m+=1
                    hand.remove(m)                    
                else:
                    return False
        
        return True                