class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums)>=k:
            return 1
        inf = 10**10

        last_pos = []
        bit_mask = []
        curmask = 1
        while curmask <= k:
            if k & curmask:
                last_pos.append(-inf)
                bit_mask.append(curmask)
            curmask *= 2

        green_bits = (bit_mask[-1]*2-1) ^ k

        bestLen = inf

        for R,x in enumerate(nums):
            xwb = x & green_bits
            if xwb:
                highest_green_bit_of_x = 1 << (xwb.bit_length() - 1)
                x = x | (highest_green_bit_of_x - 1)

            for idx,needmask in enumerate(bit_mask):
                if x & needmask:
                    last_pos[idx] = R
            bestLen = min(bestLen, R - min(last_pos) + 1)

        return bestLen if bestLen < inf else -1