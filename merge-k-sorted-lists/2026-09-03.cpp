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

struct MinListNode {
  bool operator()(const ListNode *lhs, const ListNode *rhs) const {
    return lhs->val > rhs->val;
  }
};

class Solution {
public:
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    priority_queue<ListNode *, vector<ListNode *>, MinListNode> pq;

    for (ListNode *list : lists) {
      if (list != nullptr) {
        pq.push(list);
      }
    }

    ListNode *head_res = new ListNode(0);
    ListNode *dummy_res = head_res;
    while (pq.size() != 0) {
      ListNode *next = pq.top();
      pq.pop();

      if (next->next != nullptr) {
        pq.push(next->next);
      }
      dummy_res->next = next;
      dummy_res = dummy_res->next;
    }

    return head_res->next;
  }
};
