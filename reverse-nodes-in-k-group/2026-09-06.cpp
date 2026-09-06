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
  ListNode *reverseGroup(ListNode *head, ListNode *end) {
    ListNode *prev = nullptr;
    ListNode *curr = head;
    ListNode *next = curr->next;

    while (next != end) {
      ListNode *new_next = next->next;

      curr->next = prev;
      next->next = curr;

      prev = curr;
      curr = next;
      next = new_next;
    }

    return curr;
  }

  ListNode *reverseKGroup(ListNode *head, int k) {
    ListNode *leading = head;
    ListNode *anchor = head;

    ListNode res;
    ListNode *prevGroupTail = &res;

    while (leading != nullptr) {
      bool shouldReverse = true;
      for (int i = 0; i < k; ++i) {
        if (leading == nullptr) {
          shouldReverse = false;
          break;
        }
        leading = leading->next;
      }

      if (!shouldReverse) {
        break;
      }

      ListNode *reversedHead = this->reverseGroup(anchor, leading);

      anchor->next = leading;
      prevGroupTail->next = reversedHead;

      prevGroupTail = anchor;
      anchor = leading;
    }

    return res.next;
  }
};
