class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bit_num = []
        count = 0
        while count < 64:
            if x & 1 == 1:
                bit_num.insert(0, 1)
            else:
                bit_num.insert(0, 0)
            x >>= 1
            count += 1
        def fill_bit(bit_num, n):
            if n <= 1:
                return 0
            count = 1
            for i in range(64):
                if bit_num[64-i-1] == 0:
                    count *= 2
                if count >= n:
                    bit_num[64-i-1] = 1
                    return n - count/2
        count = n
        while count > 0:
            count = fill_bit(bit_num, count)
        ret_num = 0
        for i in range(64):
            if bit_num[64-i-1] == 1:
                ret_num += 2**i
        return ret_num