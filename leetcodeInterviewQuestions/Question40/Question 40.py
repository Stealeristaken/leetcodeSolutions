class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(ind,target):
            if target==0:
                ans.append(op[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                op.append(candidates[i])
                solve(i+1,target-candidates[i])
                op.pop()

        candidates.sort()
        ans=[]
        op=[]
        solve(0,target)
        return ans
    
    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            # Base case: if target is 0, we've found a valid combination
            if target == 0:
                res.append(path[:])  # Add a copy of the current path to results
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # If current candidate is greater than target, no need to continue
                # (since candidates are sorted)
                if candidates[i] > target:
                    break
                
                # Include current candidate in the path
                path.append(candidates[i])
                
                # Recursively backtrack with updated target and start index
                backtrack(i + 1, target - candidates[i], path)
                
                # Backtrack: remove the current candidate to try next option
                path.pop()

        # Sort candidates to handle duplicates and enable early termination
        candidates.sort()
        
        # Initialize result list
        res = []
        
        # Start backtracking from index 0, with full target and empty path
        backtrack(0, target, [])
        
        return res