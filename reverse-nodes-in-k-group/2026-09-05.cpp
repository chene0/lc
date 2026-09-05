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
  bool advanceNodeByK(int k, ListNode *&node) {
    for (int i = 0; i < k; ++i) {
      if (node == nullptr) {
        return false;
      }
      node = node->next;
    }

    return true;
  }

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
      if (!this->advanceNodeByK(k, leading)) {
        break;
      }

      ListNode *reversedGroupHead = reverseGroup(anchor, leading);
      anchor->next = leading;
      prevGroupTail->next = reversedGroupHead;
      prevGroupTail = anchor;
      anchor = leading;
    }

    return res.next;
  }
};
