class Solution
{
public:
      double maxProbability(int n, vector<vector<int>> &edges, vector<double> &succProb, int start, int end)
      {

            vector<vector<pair<int, double>>> g(n);
            for (int i = 0; i < edges.size(); i++)
            {
                  int u = edges[i][0], v = edges[i][1];
                  g[u].push_back({v, succProb[i]});
                  g[v].push_back({u, succProb[i]});
            }
            priority_queue<pair<double, int>> pq;
            vector<double> dist(n, 0.0);
            pq.push({1.0, start});
            dist[start] = 1.0;
            double cnt = 1.0;
            while (!pq.empty())
            {
                  double prob = pq.top().first;
                  int node = pq.top().second;
                  pq.pop();
                  // cnt *= prob;
                  // if(node == end){
                  //     return cnt;
                  // }
                  for (auto &it : g[node])
                  {
                        int curr = it.first;
                        double p = it.second;
                        if (dist[curr] < dist[node] * p)
                        {
                              dist[curr] = dist[node] * p;
                              pq.push({dist[curr], curr});
                        }
                  }
            }
            return dist[end];
      }
};