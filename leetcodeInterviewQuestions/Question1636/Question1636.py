from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = Counter(nums)
        buckets = [[] for i in range(max(freq_dict.values()) + 1)]
        for k, v in freq_dict.items():
            for i in range(v):
                buckets[v].append(k)
        
        for l in buckets:
            l.sort(reverse=True)
        res = []
        for i in range(len(buckets)):
            if len(buckets[i]) > 0:
                res.extend(buckets[i])
        return res
        