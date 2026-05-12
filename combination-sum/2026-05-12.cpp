class Solution {
public:
  void backtrack(int idx, vector<int> &nums, int target,
                 vector<int> &running_vec, int running_sum,
                 vector<vector<int>> &res) {
    if (running_sum == target) {
      vector<int> entry(running_vec);
      res.push_back(entry);
      return;
    }

    if (running_sum > target || idx >= nums.size()) {
      return;
    }

    int num = nums[idx];

    // take
    running_vec.push_back(num);
    this->backtrack(idx, nums, target, running_vec, running_sum + num, res);
    running_vec.pop_back();

    // leave
    this->backtrack(idx + 1, nums, target, running_vec, running_sum, res);
  }

  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<vector<int>> res;
    vector<int> running_vec;

    backtrack(0, candidates, target, running_vec, 0, res);

    return res;
  }
};
