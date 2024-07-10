from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                folder_depth = max(folder_depth-1, 0)
            else:
                folder_depth += 1

        return folder_depth


        