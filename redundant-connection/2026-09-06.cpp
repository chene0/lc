class Solution {
public:
  int node_find(int node, vector<int> &parent) {
    if (node == parent[node]) {
      return node;
    }

    int common_ancestor = node_find(parent[node], parent);
    parent[node] = common_ancestor;

    return common_ancestor;
  }

  bool node_union(int a, int b, vector<int> &parent, vector<int> &rank) {
    int p_a = node_find(a, parent);
    int p_b = node_find(b, parent);

    if (p_a == p_b) {
      return false;
    }

    if (rank[p_a] == rank[p_b]) {
      parent[p_b] = p_a;
      ++rank[p_a];
    } else if (rank[p_a] > rank[p_b]) {
      parent[p_b] = p_a;
    } else {
      parent[p_a] = p_b;
    }

    return true;
  }

  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    int n = edges.size();

    vector<int> parent(n + 1);
    vector<int> rank(n + 1);

    for (int i = 0; i < n + 1; ++i) {
      parent[i] = i;
    }

    for (const vector<int> &edge : edges) {
      if (!node_union(edge[0], edge[1], parent, rank)) {
        return edge;
      }
    }

    return {};
  }
};
