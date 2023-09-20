class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:

        # sliding window solution

        # target will represent the subarray that is not needed
        # when our subarray equals to target then everything outside, will be the number of operations to reduce x to zero
        target = sum(nums) - x

        # !!! if our target is 0 then the whole array is needed to reduce x to 0 !!!
        if target == 0:
            return len(nums)

        l, r = 0, 0
        # currSum will keep track of the sum of our current subarray
        currSum = 0

        # operations will be infinite for now since we want the MINIMUM NUMBER of operations
        operations = float('inf')

        for r in range(len(nums)):
            currSum += nums[r]

            # if currSum is greater than our target then we want to shrink our window
            # also do some out of bounds checking
            while currSum >= target and l < len(nums):
                # if the current sum == target then we have the window that we don't need
                if currSum == target:
                    # update the operations
                    # the whole array - the sub array will equal to x
                    # * it represents the outside operations that can reduce x to zero
                    operations = min(operations, len(nums) - (r - l + 1))

                # shrink the window
                currSum -= nums[l]
                l += 1

        return operations if operations != float('inf') else -1

