from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b
        }

        def backtrack(left, right):
            res = []
            for i in range(left, right+1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i-1)
                    nums2 = backtrack(i+1, right)
                
                    for i in nums1:
                        for j in nums2:
                            res.append(operations[op](i, j))
            if res == []:
                res.append(int(expression[left : right+1]))
            return res

        return backtrack(0, len(expression) - 1)