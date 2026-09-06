#define NOT_VISITED 0
#define VISITING 1
#define VISITED 2

class Solution {
public:
  bool topo(char currChar, vector<int> &alphVisited, vector<char> &topoSort,
            unordered_map<char, vector<char>> &adj) {
    if (alphVisited[currChar - 'a'] == VISITING) {
      return false;
    }

    if (alphVisited[currChar - 'a'] == VISITED) {
      return true;
    }

    alphVisited[currChar - 'a'] = VISITING;

    for (char neighbourChar : adj[currChar]) {
      if (!this->topo(neighbourChar, alphVisited, topoSort, adj)) {
        return false;
      }
    }

    alphVisited[currChar - 'a'] = VISITED;
    topoSort.push_back(currChar);

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

      for (int i = 0; i < minSize; ++i) {
        if (wordA[i] != wordB[i]) {
          adj[wordA[i]].push_back(wordB[i]);
          break;
        }
      }
    }

    vector<int> alph(26);
    vector<char> topoSort;

    for (const auto &[key, _] : adj) {
      if (!this->topo(key, alph, topoSort, adj)) {
        return "";
      }
    }

    string res(topoSort.rbegin(), topoSort.rend());
    return res;
  }
};
