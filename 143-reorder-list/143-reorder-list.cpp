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
#include <stack>

class Solution {
public:
    void reorderList(ListNode* head) {
        stack<ListNode*> stack;
        ListNode* curr = head;
        int size = 0; // Keep track of the list size
        
        while(curr != nullptr) // Push all the nodes to the stack
        {
            size++;
            stack.push(curr);
            curr = curr->next;
        }
        
        curr = head;
        
        for(int i=0;i<size/2;i++) // Half of the nodes from the top of the stack get inserted into alternating positions
        {
            // Create a new node using the top of the stack (ie, starting from the end of the original list)
            ListNode* new_node = stack.top();
            stack.pop();
            
            // Insert the node between the current node and the node in front of it
            new_node->next = curr->next;
            curr->next = new_node;
            
            curr = curr->next->next; // Go 2 nodes ahead (to alternate)
        }
        curr->next = nullptr; // End of the list
    }
};