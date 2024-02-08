class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 1_000_000_007
        n = len(arr)
        ans = 0
        stack = []
        for right in range(n + 1):
            while stack and (right == n or arr[stack[-1]] >= arr[right]):
                i = stack.pop()
                left = -1 if not stack else stack[-1]
                ans = (ans + arr[i] * (i - left) * (right - i))  % M
            stack.append(right)
        return ans



#define a function that sort numbers in a list
def sortlist(list)