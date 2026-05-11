class Solution {
public:
    void backtrack(int idx, vector<int>& nums, vector<int>& running_arr, vector<vector<int>>& res) {
        if (idx >= nums.size()) {
            res.push_back(running_arr);
            return;
        }

        int num = nums[idx];

        // take
        running_arr.push_back(num);
        backtrack(idx+1, nums, running_arr, res);
        running_arr.pop_back();

        // skip
        while ( (idx+1) < nums.size() && nums[idx+1] == nums[idx] ) {
            ++idx;
        }
        backtrack(idx+1, nums, running_arr, res);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> running_arr;

        sort(nums.begin(), nums.end());        

        this->backtrack(0, nums, running_arr, res);

        return res;
    }
};
