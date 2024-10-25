class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        current = folder[0]
        result = [current]
        for path in folder[1:]:
            if path.find(current) == 0 and path[len(current)] == '/':
                continue
            result.append(path)
            current = path
        return result
            