class Solution {
public:
  int leastInterval(vector<char> &tasks, int n) {
    unordered_map<char, int> freq_dict;
    int max_freq = 0;

    for (char task : tasks) {
      if (freq_dict.find(task) == freq_dict.end()) {
        freq_dict[task] = 1;
      } else {
        freq_dict[task] += 1;
      }

      max_freq = max(max_freq, freq_dict[task]);
    }

    int num_max_freq = 0;
    for (auto it = freq_dict.begin(); it != freq_dict.end(); ++it) {
      if (it->second == max_freq) {
        num_max_freq += 1;
      }
    }

    return max((max_freq - 1) * (n + 1) + num_max_freq,
               static_cast<int>(tasks.size()));
  }
};
