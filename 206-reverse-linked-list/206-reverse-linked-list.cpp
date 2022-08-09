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
    ListNode* reverseList(ListNode* head) {
        //std::cout<<head->next->val;
        
        ListNode *curr = head; // Pointer to traverse the list
        ListNode *tmpNext = nullptr; // Temp pointer to point to the next node
        ListNode *tmpPrev = nullptr; // Temp pointer to point to the previous node
        
        while(curr != nullptr)
        {
            if(curr->next == nullptr) // If the last node is reached
                head = curr; // Set the it (the last node) as the head
            
            tmpNext = curr->next; // Set the temporary next pointer
            
            curr->next = tmpPrev; // Redirect the current node's next pointer to the previous node
            tmpPrev = curr; // Update the previous pointer to the current node to setup for the next iteration
            
            curr = tmpNext; // Go to the next node
        }
        
        return head;
    }
};