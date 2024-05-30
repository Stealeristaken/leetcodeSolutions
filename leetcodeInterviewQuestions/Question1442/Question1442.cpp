#include <unordered_map>
#include <vector>

class Solution
{
public:
      int countTriplets(std::vector<int> &arr)
      {
            int x = 0;
            int n = arr.size();
            std::unordered_map<int, std::tuple<int, int, int>> d;
            d[0] = std::make_tuple(0, -1, 0);
            int ans = 0;
            for (int i = 0; i < n; i++)
            {
                  x ^= arr[i];
                  if (d.count(x))
                  {
                        int cnt = std::get<2>(d[x]) + 1;
                        int total = std::get<0>(d[x]) + (i - std::get<1>(d[x])) * cnt;
                        ans += total - cnt;
                        d[x] = std::make_tuple(total, i, cnt);
                  }
                  else
                  {
                        d[x] = std::make_tuple(0, i, 0);
                  }
            }
            return ans;
      }
};