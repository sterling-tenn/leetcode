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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {        
        ListNode *head = nullptr; // Store the result list
        ListNode *tmpPrev = nullptr; // Keep track of the previous node since it's a singly-linked list
        
        int carry = 0; // Carry bit represents either 1 or 0 since contraints are single digits, max can be 18 + 1 carry = 19
        int sum; // Keep track of the sum for each digit
        
        while(l1 != nullptr || l2 != nullptr || carry != 0 ) // Traverse as long as one of the lists isn't finished, or there's still a carry value
        {
            ListNode *newNode = new ListNode; // Create a new node
            sum = 0; // Reset the sum for each created node
            
            if(head == nullptr) head = newNode; // Set the head if it isn't already set, ie the first node

            if(tmpPrev == nullptr) tmpPrev = head; // Set the temporary previous node counter
            else // Update the previous node to point to the newly created node
            {
                tmpPrev->next = newNode;
                tmpPrev = newNode;
            }
            
            
            // The total sum should be: sum = l1->val + l2->val + carry
            if(l1 != nullptr) // Handle if the end of the first list is reached
            {
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != nullptr) // Handle if the end of the second list is reached
            {
                sum += l2->val;
                l2 = l2->next;
            }
            sum += carry;
            
            // Assign the value to the newly created node and update the carry bit
            if(sum < 10)
            {
                carry = 0;
                newNode->val = sum;
            }
            else
            {
                newNode->val = sum%10;
                carry = 1;
            }

        }      
        return head;
    }
};