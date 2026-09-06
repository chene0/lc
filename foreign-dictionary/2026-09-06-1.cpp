enum class CharState { NOT_VISITED, VISITING, VISITED };

class Solution {
public:
  bool topo(char curr, vector<CharState> &alphVisited, vector<char> &res,
            const unordered_map<char, vector<char>> &adj) {
    int currIdx = curr - 'a';

    if (alphVisited[currIdx] == CharState::VISITED) {
      return true;
    }

    if (alphVisited[currIdx] == CharState::VISITING) {
      return false;
    }

    alphVisited[currIdx] = CharState::VISITING;

    for (char neighbour : adj.at(curr)) {
      if (!this->topo(neighbour, alphVisited, res, adj)) {
        return false;
      }
    }

    alphVisited[currIdx] = CharState::VISITED;
    res.push_back(curr);

    return true;
  }

  string foreignDictionary(vector<string> &words) {
    unordered_map<char, vector<char>> adj;

    for (string word : words) {
      for (char c : word) {
        adj[c];
      }
    }

    for (int i = 0; i < words.size() - 1; ++i) {
      auto [wordA, wordB] = tie(words[i], words[i + 1]);
      int minSize = min(wordA.size(), wordB.size());

      if (wordA.substr(0, minSize) == wordB.substr(0, minSize) &&
          wordA.size() > wordB.size()) {
        return "";
      }

      for (int j = 0; j < minSize; ++j) {
        if (wordA[j] != wordB[j]) {
          adj[wordA[j]].push_back(wordB[j]);
          break;
        }
      }
    }

    vector<CharState> alphVisited(26);
    vector<char> topoSort;

    for (const auto &[key, _] : adj) {
      if (!this->topo(key, alphVisited, topoSort, adj)) {
        return "";
      }
    }

    string res(topoSort.rbegin(), topoSort.rend());
    return res;
  }
};
