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
    void reorderList(ListNode* head) {
        if (head->next == nullptr) {
            return;
        }

        ListNode* h = head;
        ListNode* t = head;

        while (h->next != nullptr && h->next->next != nullptr) {
            h = h->next->next;
            t = t->next;
        }

        ListNode* m = t->next;
        t->next = nullptr;

        ListNode* prev = nullptr;
        ListNode* curr = m;
        ListNode* nxt = m->next;

        while (nxt != nullptr) {
            ListNode* nxt_next = nxt->next;

            curr->next = prev;
            nxt->next = curr;

            prev = curr;
            curr = nxt;
            nxt = nxt_next;
        }

        m = curr;

        ListNode* d = head;
        while (d != nullptr && m != nullptr) {
            ListNode* d_next = d->next;
            ListNode* m_next = m->next;
            
            d->next = m;
            m->next = d_next;

            d = d_next;
            m = m_next;
        }
    }
};
