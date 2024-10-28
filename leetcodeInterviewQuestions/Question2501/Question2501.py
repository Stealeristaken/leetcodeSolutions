class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        max_length = 0
        n = len(unique_nums)
        
        num_set = set(unique_nums)

        for i in range(n):
            streak_length = 1
            current = unique_nums[i]
            
            while True:
                next_value = current ** 2
                if next_value in num_set:
                    streak_length += 1
                    current = next_value
                else:
                    break
            
            if streak_length >= 2:
                max_length = max(max_length, streak_length)
        
        return max_length if max_length >= 2 else -1