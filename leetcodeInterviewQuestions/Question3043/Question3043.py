class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = set(arr2)
        arr1_prefixes = set()
        for el in arr1:
            while el not in arr1_prefixes and el > 0:
                arr1_prefixes.add(el)
                el //= 10

        max_length = 0
        for el in arr2:
            # Keep searching until we find one
            while el not in arr1_prefixes and el > 0:
                el //= 10
            if el > 0:
                max_length = len(str(el)) if len(str(el)) > max_length else max_length

        return max_length

        