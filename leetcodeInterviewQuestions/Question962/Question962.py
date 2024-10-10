class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        indices_stack = []

        # Fill the stack with indices in increasing order of their values
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)
        # print("This is our initial indices_stack", indices_stack)
        max_width = 0

        # Traverse the array from the end to the start
        for j in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                # print("Our indices_stack looks like this: ", indices_stack, "and we just determined that our last index:",indices_stack[-1], "which corresponds to the number", nums[indices_stack[-1]], "is less than our nums[j]:", nums[j])
                # print("So lets input a max", j - indices_stack[-1])
                max_width = max(max_width, j - indices_stack[-1])
                # Pop the index since it's already processed
                indices_stack.pop()
            # if indices_stack:
            #     print("However in our stack", indices_stack[-1], "which is", nums[indices_stack[-1]], "is not less than our current j", j, "which is", nums[j])
        return max_width