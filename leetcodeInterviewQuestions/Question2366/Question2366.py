class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the array
        operations = 0  # Initialize the operations counter

        prevValue = nums[n - 1]  # Initialize prevValue with the last element of the array

        # Iterate through the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > prevValue:
                # Calculate how many times prevValue should be added to get nums[i]
                k = (nums[i] + prevValue - 1) // prevValue
                # Increment operations by k - 1
                operations += k - 1
                # Update prevValue to be nums[i] divided by k
                prevValue = nums[i] // k
            else:
                # If nums[i] is not greater than prevValue, update prevValue to nums[i]
                prevValue = nums[i]

        return operations  # Return the total number of operations
