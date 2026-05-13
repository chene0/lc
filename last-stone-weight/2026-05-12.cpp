class Solution {
public:
  int lastStoneWeight(vector<int> &stones) {
    make_heap(stones.begin(), stones.end());

    while (stones.size() > 1) {
      pop_heap(stones.begin(), stones.end());
      int a = stones.back();
      stones.pop_back();

      pop_heap(stones.begin(), stones.end());
      int b = stones.back();
      stones.pop_back();

      int diff = abs(a - b);

      stones.push_back(diff);
      push_heap(stones.begin(), stones.end());
    }

    return *(stones.begin());
  }
};
