class Solution:
      def maxLength(self, arr: List[str]) -> int:
        def checkUnique(s):
            return len(s) == len(set(s))
        
        def dfs(arr, index, path):
            if index == len(arr):
                return len(path)
            
            ans = dfs(arr, index + 1, path)
            if checkUnique(arr[index] + path):
                ans = max(ans, dfs(arr, index + 1, arr[index] + path))
                
            return ans
        
        return dfs(arr, 0, "")