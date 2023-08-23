
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # Define a flag for handling negative numbers
        negative_flag = False
        if x < 0:
            negative_flag = True
            x = abs(x)

        # Reverse the digits
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # Apply the negative sign if needed
        if negative_flag:
            reversed_x = -reversed_x

        # Check if the reversed number is within the 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x