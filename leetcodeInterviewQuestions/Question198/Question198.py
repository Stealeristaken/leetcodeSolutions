class Solution:
    def rob(self, nums: List[int])->int:
        bag = (0,0)

        for house in nums:
            bag=(bag[1], max(bag[0]+house, bag[1]))
        return bag[1]
            
