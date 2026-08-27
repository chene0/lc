class Solution {
public:
  int reverse(int x) {
    int res = 0;

    while (x != 0) {
      int lsb = x % 10;
      x /= 10;

      if (res > INT_MAX / 10 || (res == INT_MAX / 10 && lsb > INT_MAX % 10)) {
        return 0;
      }

      if (res < INT_MIN / 10 || (res == INT_MIN / 10 && lsb < INT_MIN % 10)) {
        return 0;
      }

      res = res * 10 + lsb;
    }

    return res;
  }
};
