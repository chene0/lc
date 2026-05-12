/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
  Node *copyRandomList(Node *head) {
    if (head == nullptr) {
      return nullptr;
    }

    unordered_map<Node *, Node *> map;

    Node *head_clone = new Node(head->val);
    map[head] = head_clone;
    Node *dummy = head->next;

    while (dummy != nullptr) {
      Node *clone = new Node(dummy->val);
      map[dummy] = clone;

      dummy = dummy->next;
    }

    dummy = head;
    while (dummy != nullptr) {
      Node *clone = map[dummy];
      Node *clone_next = map[dummy->next];
      Node *clone_random = map[dummy->random];

      clone->next = clone_next;
      clone->random = clone_random;

      dummy = dummy->next;
    }

    return head_clone;
  }
};
