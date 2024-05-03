class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
            v1 = list(map(int, version1.split('.')))
            v2 = list(map(int, version2.split('.')))
            n = max(len(v1), len(v2))
            v1 += [0] * (n - len(v1))
            v2 += [0] * (n - len(v2))
            for i in range(n):
                  if v1[i] < v2[i]:
                   return -1
                  elif v1[i] > v2[i]:
                   return 1
            return 0
      
      
#########################   
      
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        ml = min(len(version1), len(version2))
        for i in range(ml):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        version = version1 if len(version1) - ml > 0 else version2
        v = 1 if len(version1) - ml > 0 else 2
        for i in range(ml, len(version)):
            if int(version[i]) > 0:
                return 1 if v == 1 else -1 
        return 0