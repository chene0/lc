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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* tort = head;
        ListNode* hare = head;

        for (int i = 0; i < n; ++i) {
            hare = hare->next;

            if (hare == nullptr) {
                return head->next;
            }
        }

        while (hare != nullptr && hare->next != nullptr) {
            hare = hare->next;
            tort = tort->next;
        }

        tort->next = tort->next->next;

        return head;
    }
};
