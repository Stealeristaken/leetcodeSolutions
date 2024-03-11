class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for num in arr:
            hashmap[num] = 1 + hashmap.get(num, 0)

        return len(hashmap.values()) == len(set(hashmap.values()))