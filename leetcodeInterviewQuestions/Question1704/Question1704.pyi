class Solution:
    def countVowel(self, s:str)->int:
        v="aeiouAEIOU"
        count=0
        for i in s:
            if(i in v):
                count+=1
        return count
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)//2
        s1=s[:l]
        s2=s[l:]
        a=self.countVowel(s1)
        b=self.countVowel(s2)
        if (a==b):
            return True
        return False