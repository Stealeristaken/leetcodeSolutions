class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        counter = collections.defaultdict(int)

        l1, l2 = len(nums1), len(nums2)

        for i in range(l1):
            counter[nums1[i]] += l2
        for i in range(l2):
            counter[nums2[i]] += l1
        
        res = 0
        for number, count in counter.items():
            if count % 2:
                res ^= number
        return res