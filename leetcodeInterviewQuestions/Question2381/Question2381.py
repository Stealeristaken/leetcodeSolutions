ORD_A = ord("a")

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            changes[start] += direction + direction - 1
            changes[end+1] -= direction + direction - 1

        return "".join(
            chr(ORD_A + ((ord(c) - ORD_A + shift) % 26))
            for c, shift in zip(s, accumulate(changes))
        )