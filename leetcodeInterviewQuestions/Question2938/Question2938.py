class Solution:
    def minimumSteps(self, s: str) -> int:
        s=s[::-1]
        start=-1
        ans=0
        for a in range(len(s)):
            if s[a]=='1':
                print(a,start)
                ans+=(a-start-1)
                start=start+1
        return ans
            