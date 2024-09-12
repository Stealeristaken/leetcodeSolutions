class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        occur = [False] * 26
        count = 0
        
        for c in allowed:
            occur[ord(c) - ord('a')] = True
        
        for word in words:
            if self.check(word, occur):
                count += 1
        
        return count
    
    def check(self, word: str, occur: List[bool]) -> bool:
        for c in word:
            if not occur[ord(c) - ord('a')]:
                return False
        return True

def main():
    input_data = sys.stdin.read().strip().split('\n')
    results = []
    
    i = 0
    while i < len(input_data):
        allowed = json.loads(input_data[i])
        words = json.loads(input_data[i + 1])
        result = Solution().countConsistentStrings(allowed, words)
        results.append(result)
        i += 2

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)