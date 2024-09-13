class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        
        n = len(a)
        prefix = [0 for i in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i] ^ a[i]

        m = len(q)
        ans = []
        for l, r in q:
            ans.append(prefix[r+1] ^ prefix[l])

        return ans