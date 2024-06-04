class Solution
{
public:
      int longestPalindrome(string s)
      {
            unordered_map<char, int> u;
            for (int i = 0; i < s.length(); i++)
            {
                  u[s[i]]++;
            }

            int ans = 0;
            bool c = true;
            int maxi = INT_MIN;
            for (auto i : u)
            {
                  if (i.second % 2 == 0)
                        ans += i.second;
                  else
                  {
                        c = false;
                        maxi = max(INT_MIN, i.second);
                        ans += (maxi - 1);
                  }
            }
            if (!c)
                  ans += 1;
            return ans;
      }
};