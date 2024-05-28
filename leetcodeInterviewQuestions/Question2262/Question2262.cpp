class Solution
{
public:
      long long number_of_subarrays(int n)
      {

            if (n < 2)
            {
                  if (n < 1)
                  {
                        return 0;
                  }
                  else
                  {
                        return 1;
                  }
            }
            return (long long)n * (n + 1) / 2;
      }

      long long appealSum(string s)
      {
            long long cnt = 0;
            long long tot_not = 0;
            set<char> se;
            for (int i = 0; i < s.length(); i++)
            {
                  se.insert(s[i]);
            }

            for (auto c = se.begin(); c != se.end(); c++)
            {
                  for (int i = 0; i < s.length(); i++)
                  {
                        long long contri = 0;
                        while (s[i] != *c && (i < s.length()))
                        {
                              contri++;
                              i++;
                        }
                        if (contri)
                        {
                              tot_not += number_of_subarrays(contri);
                        }
                  }
            }
            long long tot = number_of_subarrays(s.length());
            long long tot_in_which_each_alphabet_prsent = (tot * se.size()) - tot_not;
            return tot_in_which_each_alphabet_prsent;
      }
};

class Solution
{
public:
      long long appealSum(string s)
      {
            ios_base::sync_with_stdio(false);
            cin.tie(nullptr);
            cout.tie(nullptr);
            long long res = 0;
            vector<int> list(26, -1);
            int size = s.size();
            long long sum = 0;
            for (int i = 0; i < size; i++)
            {
                  int &a = list[s[i] - 'a'];
                  sum += i - a;
                  res += sum;
                  a = i;
            }
            return res;
      }
};