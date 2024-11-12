class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0])
        mp = {}
        prices = []
        maxi = -1
        for i in items:
            if i[0] not in mp:
                prices.append(i[0])
            maxi = max(maxi,i[1])
            mp[i[0]] = maxi

        ans = []
        for i in queries:
            if i in mp:
                ans.append(mp[i])
            else:
                ind = bisect.bisect_left(prices,i)
                if ind == 0:
                    ans.append(0)
                else:
                    key = prices[ind-1]
                    ans.append(mp[key])
        return ans

        
        