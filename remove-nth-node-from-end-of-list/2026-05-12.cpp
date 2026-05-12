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
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode *hare = head;
    ListNode *tort = head;

    for (int i = 0; i < n + 1; ++i) {
      if (hare == nullptr) {
        return head->next;
      }
      hare = hare->next;
    }

    while (hare != nullptr) {
      hare = hare->next;
      tort = tort->next;
    }

    tort->next = tort->next->next;

    return head;
  }
};
