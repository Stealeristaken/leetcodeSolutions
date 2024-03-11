class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output=[]
        for i in range(n):
            output.extend([nums[i],nums[i+n]])
        return output