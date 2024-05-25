from typing import List



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def f(i,sentence):
            if i == len(s):
                res.append(''.join(sentence).lstrip())
                return
            for j in range(i+1,len(s)+2):
                if s[i:j] in wordDict:
                    f(j,sentence+[" "]+[s[i:j]])
        f(0,[])
        return res
        