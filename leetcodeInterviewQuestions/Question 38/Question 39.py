class Solution:
    def countAndSay(self, n: int) -> str:
        result='1'
        for n in range(2,n+1):
            count=0
            target=result[0]
            ans=''
            for _ in result:
                if _==target:
                    count+=1
                else:
                    ans+=str(count)+target
                    count=1
                    target=_
            ans+=str(count)+target
            result=ans
        return result