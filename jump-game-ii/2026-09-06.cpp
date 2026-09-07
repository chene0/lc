class Solution {
public:
  int jump(vector<int> &nums) {
    int currEnd = 0;
    int nextEnd = 0;
    int res = 0;

    for (int i = 0; i < nums.size() - 1; ++i) {
      nextEnd = max(nextEnd, nums[i] + i);

      if (i == currEnd) {
        ++res;
        currEnd = nextEnd;
      }
    }

    return res;
  }
};
