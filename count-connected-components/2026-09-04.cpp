class Solution {
public:
  int node_find(int a, vector<int> &parents) {
    if (a == parents[a]) {
      return a;
    }

    int common_ancestor = node_find(parents[a], parents);
    parents[a] = common_ancestor;
    return common_ancestor;
  }

  bool node_union(int a, int b, vector<int> &parents, vector<int> &ranks) {
    int p_a = node_find(a, parents);
    int p_b = node_find(b, parents);

    if (p_a == p_b) {
      return false;
    }

    if (ranks[p_a] == ranks[p_b]) {
      ++ranks[p_a];
      parents[p_b] = p_a;
    } else if (ranks[p_a] > ranks[p_b]) {
      parents[p_b] = p_a;
    } else {
      parents[p_a] = p_b;
    }

    return true;
  }

  int countComponents(int n, vector<vector<int>> &edges) {
    vector<int> ranks(n);
    vector<int> parents(n);
    int num_components = n;

    for (int i = 0; i < n; ++i) {
      parents[i] = i;
    }

    for (const vector<int> &edge : edges) {
      if (node_union(edge[0], edge[1], parents, ranks)) {
        --num_components;
      }
    }

    return num_components;
  }
};
