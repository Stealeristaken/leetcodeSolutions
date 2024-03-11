class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        decreasingStack = deque()
        maxThirdElement = float('-inf')
        for i in range(length - 1, -1, -1):
            currentNumber = nums[i]

            if currentNumber < maxThirdElement:
                return True

            while decreasingStack and decreasingStack[0] < currentNumber:
                maxThirdElement = decreasingStack.popleft()

            decreasingStack.appendleft(currentNumber)

        return False