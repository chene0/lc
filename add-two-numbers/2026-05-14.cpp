/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int carry = 0;

    ListNode *res = new ListNode();
    ListNode *dummy = res;

    while (l1 != nullptr && l2 != nullptr) {
      int sum = l1->val + l2->val + carry;
      carry = floor(sum / 10);

      dummy->next = new ListNode(sum % 10);
      dummy = dummy->next;

      l1 = l1->next;
      l2 = l2->next;
    }

    while (l1 != nullptr) {
      int sum = l1->val + carry;
      carry = floor(sum / 10);

      dummy->next = new ListNode(sum % 10);
      dummy = dummy->next;

      l1 = l1->next;
    }

    while (l2 != nullptr) {
      int sum = l2->val + carry;
      carry = floor(sum / 10);

      dummy->next = new ListNode(sum % 10);
      dummy = dummy->next;

      l2 = l2->next;
    }

    if (carry > 0) {
      dummy->next = new ListNode(carry);
    }

    return res->next;
  }
};
