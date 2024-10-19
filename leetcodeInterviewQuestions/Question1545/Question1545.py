class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findKthBitRecursive(n, k):
            if n == 1: 
                return '0'
            length = (1 << n) - 1 
            mid = length // 2 + 1 
            
            if k == mid: 
                return '1'
            elif k < mid:  
                return findKthBitRecursive(n - 1, k)
            else:  
                mirrored_position = length - k + 1
                return '0' if findKthBitRecursive(n - 1, mirrored_position) == '1' else '1'
        
        return findKthBitRecursive(n, k)