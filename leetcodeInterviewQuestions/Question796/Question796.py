class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal): return False
        if Counter(goal) != Counter(s): return False
        hm = defaultdict(list)
        for i, c in enumerate(goal): hm[c].append(i)
        for i in hm[s[0]]:
            for c in s:
                if c != goal[i]: break
                i += 1
                i %= n
            else: return True
        return False