class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos, neg = [], []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        nums[0 : len(pos) * 2 : 2] = pos
        nums[1 : len(neg) * 2 : 2] = neg

        return nums
  
  
  
  
  
##########
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        i_pos, i_neg = 0, 1
        for num in nums:
            if num > 0:
                i = i_pos
                i_pos += 2
            else:
                i = i_neg
                i_neg += 2

            result[i] = num
        
        return result