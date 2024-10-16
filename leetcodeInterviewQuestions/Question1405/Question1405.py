class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        maxh = []
        if a:
            heappush(maxh, (-a, 'a'))
        if b:
            heappush(maxh, (-b, 'b'))
        if c:
            heappush(maxh, (-c, 'c'))

        res = ""
        while maxh:
            f1, c1 = heapq.heappop(maxh)
            f1 *= -1

            if len(res)>=2 and res[-1]==res[-2]==c1:
                if not maxh:
                    return res
                f2, c2 = heapq.heappop(maxh)
                f2 *= -1
                res += c2
                f2 -= 1
                if f2:
                    heapq.heappush(maxh,(-1*f2, c2))
                heapq.heappush(maxh,(-1*f1, c1))
                continue


            res += c1
            f1 -= 1
            if f1:
                heapq.heappush(maxh,(-1*f1, c1))

        return res