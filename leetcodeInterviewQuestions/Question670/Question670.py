class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        total_digits = len(digits)
        digits2indices = dict()
        for idx, digit in enumerate(digits):
            if digit not in digits2indices.keys():
                digits2indices.update({digit: []})
            digits2indices[digit].append(idx)

        digits2indices = dict(sorted(digits2indices.items(), reverse=True))
        current_idx = 0
        for digit, indices in digits2indices.items():
            for idx in indices[::-1]:  # Key: put bigger indices to the front if possible.
                while current_idx < total_digits - 1 and current_idx <= idx:
                    if digits[current_idx] < digits[idx]:
                        digits[current_idx], digits[idx] = digits[idx], digits[current_idx]
                        return int("".join(digits))
                    
                    if digits[current_idx] == digits[idx]:
                        current_idx += 1
                        continue
                
                if current_idx == total_digits - 1:
                    return int("".join(digits))