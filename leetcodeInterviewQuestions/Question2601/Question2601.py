class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        import bisect
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isIncreasing(nums):
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    return False
            return True
        def buildPrimes(n):
            primes, res = [True for i in range(max_n)], []
            p = 2
            while p * p < n:
                if primes[p] == True:
                    for i in range(p*p, n, p):
                        primes[i] = False
                p += 1
            for i,v in enumerate(primes):
                if v == True and i not in [0,1]:
                    res.append(i)
            return res
        def search(primes, a, b):
            diff = a-b
            return bisect.bisect_right(primes, diff)
        if isIncreasing(nums):
            return True 
        max_n = 1001
        primes = buildPrimes(max_n)
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= nums[i+1]:
                v = search(primes, nums[i], nums[i+1])
                if v >= len(primes) or nums[i] <= primes[v]:
                    return False
                nums[i] -= primes[v]
        return nums[0] < nums[1]