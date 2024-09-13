class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        
        n = len(a)
        prefix = [0 for i in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i] ^ a[i]

        m = len(q)
        ans = []
        for l, r in q:
            ans.append(prefix[r+1] ^ prefix[l])

        return ans
  
  
class Solution:
    def xorQueries(self, arr, queries):
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ arr[i]
        
        xor = []
        for l, r in queries:
            if l > 0:
                xor.append(arr[r] ^ arr[l-1])
            else:
                xor.append(arr[r])
        
        return xor

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        queries = json.loads(lines[i*2 + 1])
        
        result = Solution().xorQueries(arr, queries)
        results.append(json.dumps(result, separators=(',', ':')))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)