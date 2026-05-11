class Solution {
public:
    void backtrack(vector<int>& nums, vector<int>& running_vec, vector<vector<int>>& res) {
        if (running_vec.size() >= nums.size()) {
            res.push_back(running_vec);
            return;
        }

        for (int num : nums) {
            if (find(running_vec.begin(), running_vec.end(), num) != running_vec.end()) {
                continue;
            }

            running_vec.push_back(num);
            backtrack(nums, running_vec, res);
            running_vec.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> running_vec;

        backtrack(nums, running_vec, res);

        return res;
    }
};
