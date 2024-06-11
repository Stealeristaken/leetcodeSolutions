class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        r = []
        f = Counter(arr1)
        for k in arr2:
            r += [k] * f[k]
            del f[k]
        for k in sorted(f):
            r += [k] * f[k]
        return r
        