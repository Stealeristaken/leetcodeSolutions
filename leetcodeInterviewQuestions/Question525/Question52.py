class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}  # Initialize count dictionary with 0 at index -1
        max_length = 0
        balance = 0

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            if balance in count:
                max_length = max(max_length, i - count[balance])
            else:
                count[balance] = i

        return max_length
  
  
  
