#include <cstddef>

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) {
            return;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* second = slow->next;
        slow->next = nullptr;

        ListNode* prev = nullptr;
        while (second) {
            ListNode* next_node = second->next;
            second->next = prev;
            prev = second;
            second = next_node;
        }

        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* next_first = first->next;
            ListNode* next_second = second->next;

            first->next = second;
            second->next = next_first;

            first = next_first;
            second = next_second;
        }
    }
};

