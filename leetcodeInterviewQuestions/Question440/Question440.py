class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k-=1
        while k>0:
            step, first, last = 0, cur, cur+1
            while first <=n:
                step +=min(n+1, last) - first
                first *=10
                last *=10
            if step <=k:
                cur+=1
                k-=step
            else:
                cur*=10
                k-=1
        
        return cur