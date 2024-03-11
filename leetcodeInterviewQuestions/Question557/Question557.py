class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()
        res = []
        for string in strList:
            res.append(string[::-1])
        return ' '.join(res)