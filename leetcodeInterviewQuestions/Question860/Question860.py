class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = ten_dollar = 0
        for i in bills:
            if i == 5: 
                five_dollar += 1
            elif five_dollar == 0: 
                return False
            elif i == 10: 
                ten_dollar += 1
                five_dollar -= 1
            else:
                if ten_dollar == 0 and five_dollar < 3:
                    return False
                elif ten_dollar == 0:
                    five_dollar -= 3
                else:
                    five_dollar -= 1
                    ten_dollar -= 1
        return True