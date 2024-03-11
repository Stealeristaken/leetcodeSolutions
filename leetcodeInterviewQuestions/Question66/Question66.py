class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver=1
        n=len(digits)

        for i in range(n):
            if digits[n-i-1]+carryOver!=10:
                digits[n-i-1]+=carryOver
                carryOver=0
                break
            else:
                digits[n-i-1]=0
        if carryOver==1:
            digits.insert(0,1)
        return digits
