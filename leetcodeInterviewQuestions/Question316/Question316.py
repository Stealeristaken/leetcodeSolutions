class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastOccurence = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char in stack:
                continue

            while stack and char < stack[-1] and i < lastOccurence[stack[-1]]:
                stack.pop()

            stack.append(char)

        return ''.join(stack)