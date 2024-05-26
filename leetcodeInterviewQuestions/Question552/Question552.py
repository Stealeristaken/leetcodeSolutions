@lru_cache(maxsize = None)
def f(n, a, l):
    if n == 0:
        return 1
    ans = 0
    # try P
    ans = (ans + f(n - 1, a, 0)) % 1000000007
    # try A if a < 2
    if a + 1 < 2:
        ans = (ans + f(n - 1, a + 1, 0)) % 1000000007
    # try L if current l < 3
    if l + 1 < 3:
        ans = (ans + f(n - 1, a, l + 1)) % 1000000007
    return ans
class Solution:
    def checkRecord(self, n: int) -> int:
        return f(n, 0, 0)     
  
  
  
##############################################################################################################################



class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9+7)
        def matmul(A, B):
            C = [[0 for _ in range(6)] for _ in range(6)]
            for k in range(6):
                for i in range(6):
                    for j in range(6): C[i][j] = (C[i][j]+A[i][k]*B[k][j])%MOD
            return C
        def pow(A, n):
            if n==1: return A
            t = pow(A, int(n/2))
            t = matmul(t, t)
            if (n%2)==0: return t
            else: return matmul(A, t)
        t = pow([[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]], n)
        return sum([t[i][0] for i in range(6)])%MOD
        