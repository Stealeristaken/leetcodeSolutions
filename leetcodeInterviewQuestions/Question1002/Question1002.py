from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[]
        for i in words[0]:
            a=words[0].count(i)
            k=1
            sum=1
            while k<len(words):
                if words[k].count(i)!=0 and i not in l:
                    sum+=1
                    if words[k].count(i)<a:
                        a=words[k].count(i)
                k+=1
            if sum==len(words):
                    l+=i*a
        return l