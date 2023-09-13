/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == nullptr || head->next == nullptr) return false;
        
        ListNode* slowPtr = head; // Acts also as current
        ListNode* fastPtr = head->next;
        
        while(true){
            if(slowPtr == nullptr || fastPtr == nullptr || fastPtr->next == nullptr) return false;
            if(slowPtr == fastPtr) return true;
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
        }
    }
};