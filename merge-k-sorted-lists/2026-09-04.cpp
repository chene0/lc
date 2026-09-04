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

    ListNode res_head;
    ListNode *res_dummy = &res_head;
    while (!pq.empty()) {
      ListNode *next_node = pq.top();
      pq.pop();

      res_dummy->next = next_node;
      res_dummy = res_dummy->next;
      if (next_node->next != nullptr) {
        pq.push(next_node->next);
      }
    }

    return res_head.next;
  }
};
