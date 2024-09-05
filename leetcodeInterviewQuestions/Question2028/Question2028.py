class Solution:
    def missingRolls(self, r: List[int], m: int, n: int) -> List[int]:
        return[]if(s:=m*(len(r)+n)-sum(r))<n or s>6*n else[s//n+(i<s%n)for i in range(n)]