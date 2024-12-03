class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        start = 0  

        for space in spaces:
           result.append(s[start:space])
           start = space 


        result.append(s[start:])
        finalAns = " ".join(result)
        return finalAns
        