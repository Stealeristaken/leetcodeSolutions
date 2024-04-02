class Solution:
      def isIsomorphic(self, s: str, t: str) -> bool:
          return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    
########## Another Solution ##########


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char, t_char = s[i], t[i]
            if s_char not in s_to_t and t_char not in t_to_s:
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char
            elif s_to_t.get(s_char) != t_char or t_to_s.get(t_char) != s_char:
                return False
        return True