class Solution:
    def __init__(self):
        self.ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
        self.tens = ["", "Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
        self.thousands = ["", " Thousand", " Million", " Billion"]

    def numberToWords(self, num: int) -> str:
        def dfs(n):
            if n < 20: return self.ones[n]
            elif n < 100: return self.tens[n // 10] + dfs(n % 10)
            elif n < 1000:
                return dfs(n // 100) + " Hundred" + dfs(n % 100)
            else:
                for i in range(3, 0, -1):
                    if n >= 1000 ** i:
                        return dfs(n // (1000 ** i)) + self.thousands[i] + dfs(n % (1000 ** i))
                return ""

        if num == 0:
            return "Zero"

        return dfs(num).lstrip()