from typing import List

class Solution:

    def is_pal(self, s: str) -> bool:
        lo = 0
        hi = len(s)-1
        for i in range(len(s)//2):
            if s[lo] != s[hi]: return False
            lo += 1
            hi -= 1
        return True

    def part_pal(self, s, l):
        def backtrack(start, current_partition):
            # If we've reached the end of the string, add the current partition to results
            if start == len(s):
                res.append(current_partition[:])
                return
            
            # Iterate over the end indices of palindromes starting at the current index
            for end in l[start]:
                # Add the current palindrome to the partition
                current_partition.append(s[start:end+1])
                # Recur for the next part of the string
                backtrack(end + 1, current_partition)
                # Backtrack to try the next palindrome partition
                current_partition.pop()

        res = []
        backtrack(0, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        pals = [set([i]) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.is_pal(sub):
                    pals[i].add(j)

        res = self.part_pal(s, pals)

        


        return res
  
  
  
##############################

class Solution:
    def __init__(self):
        self.ans = {}
        
    def partition(self, s: str) -> List[List[str]]:
        if(s in self.ans):
            return self.ans[s]
        
        if(len(s) == 0):
             result = [[]]
        elif(len(s) == 1):
             result = [[s]]
        else:
            result = []
            for i in range(1, len(s) + 1):  
                left = []
                if(s[:i] == "".join(reversed(s[:i]))):
                    left.append([s[:i]])

                right = self.partition(s[i:])

                for l in left:
                    for r in right:
                        result.append(l + r)
        
        self.ans[s] = result
        return result
        