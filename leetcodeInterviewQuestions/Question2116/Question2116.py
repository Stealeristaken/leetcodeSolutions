class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        balance = 0
        flexible = 0

        for i in range(len(s)):
            if locked[i] == '1':
                balance += 1 if s[i] == '(' else -1
            else:
                flexible += 1
            if balance + flexible < 0:
                return False
        
        balance = 0
        flexible = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                balance += 1 if s[i] == ')' else -1
            else:
                flexible += 1
            if balance + flexible < 0:
                return False
        return True

        