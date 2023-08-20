# Question 1 - Two Sum:

class Solution:
    def twoSum(self, nums, target):
        # Create a hash table to store the indices of the elements
        hash_table = {}

        # Iterate through the list of nums
        for i, num in enumerate(nums):
            # Check if target - num is in the hash table
            if target - num in hash_table:
                # If it is, return the indices of the two numbers
                return [hash_table[target - num], i]
            # Otherwise, add the current element and its index to the hash table
            hash_table[num] = i

        # If we reach here, it means we didn't find a solution
        return []