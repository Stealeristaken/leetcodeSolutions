class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_dict = {}
        non_distinct = set()
        count = 0 

        for string in arr:
            freq_dict[string] = freq_dict.get(string, 0) + 1
        
        for keys in freq_dict.keys():
            if freq_dict[keys] != 1 and keys not in non_distinct:
                non_distinct.add(keys)

        for string in arr:
            if string in non_distinct:
                continue
            count += 1 
            if count == k:
                return string 
            
        
        return ""