class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit = ''.join(str(ord(chr) - 96) for chr in s)
        for _ in range(k):
            num = 0
            for i in digit:
                num+=int(i)
                digit = str(num)
        return num