class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        take i [i=0 so no need but in case of sublists] and j expanding window of list
        keep doing xor operation of split list from i to j
        append xor k <2^maxbit  (a)
        keep appending to ans
        return reverse of ans
        """
        a=(1 << maximumBit) - 1
        ans = []
        x = 0
        for j in range(len(nums)):
            x ^= nums[j]
            k = x^a
            ans.append(k)
        return ans[::-1]