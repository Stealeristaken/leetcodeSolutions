class Solution:
    def missingRolls(self, r: List[int], m: int, n: int) -> List[int]:
        return[]if(s:=m*(len(r)+n)-sum(r))<n or s>6*n else[s//n+(i<s%n)for i in range(n)]
  
  
  
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        totalSum = mean * (m + n)
        rollsSum = sum(rolls)
        
        missingSum = totalSum - rollsSum
        
        if missingSum < n or missingSum > 6 * n:
            return []
        
        quotient, remainder = divmod(missingSum, n)
        return [quotient + (1 if i < remainder else 0) for i in range(n)]

def main():
    inputs = map(loads, sys.stdin)
    results = []

    while True:
        try:
            rolls = next(inputs)
            mean = next(inputs)
            n = next(inputs)
            
            result = Solution().missingRolls(rolls, mean, n)
            results.append(result)
        except StopIteration:
            break

    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)

if __name__ == "__main__":
    main()
    sys.exit(0)