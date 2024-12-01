class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  
        for nums in arr: 
            if nums*2 in seen or nums/2 in seen:
                return True
            seen.add(nums)
        return False 