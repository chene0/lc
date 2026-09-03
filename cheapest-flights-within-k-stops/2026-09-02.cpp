class Solution {
public:
  int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst,
                        int k) {
    vector<int> costs(n, numeric_limits<int>::max());
    costs[src] = 0;

    for (int i = 0; i < k + 1; ++i) {
      vector<int> costs_tmp = costs;

      for (vector<int> &flight : flights) {
        auto [from, to, price] = tie(flight[0], flight[1], flight[2]);
        if (costs[from] == INT_MAX) {
          continue;
        }

        costs_tmp[to] = min(costs_tmp[to], price + costs[from]);
      }

      costs = costs_tmp;
    }

    return (costs[dst] != numeric_limits<int>::max()) ? costs[dst] : -1;
  }
};
