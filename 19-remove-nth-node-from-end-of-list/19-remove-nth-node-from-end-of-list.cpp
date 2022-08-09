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
        ListNode *curr = head; // Keep track of the current node
        ListNode *tmpPrev = nullptr; // To keep track of the previous node
        int length = getLength(head); // Get the length of the linked list
        int nodeCounter = 1; // Keep track of where the current node is
        while(curr != nullptr)
        {
            if(nodeCounter == length - n + 1) // Compare with the nth node from the end
            {
                if(length - n != 0) // If the node being removed is not the first one in the list
                    tmpPrev->next = curr->next; // Set the previous node's next node to skip the current node
                else // Edge case where the previous node pointer was not pointing to a node
                    head = curr->next;
                delete curr; // Delete the removed node from memory
                break; // Exit the while loop
            }
            
            tmpPrev = curr; // Update the previous node pointer
            curr = curr->next; // Go to the next node
            nodeCounter++; // Increment the node counter
        }
        return head;
    }
private:
    int getLength(ListNode* head){ // Get the node length of the linked list
        int counter = 0;
        ListNode* curr = head;
        while(curr != nullptr)
        {
            counter++;
            curr = curr->next;
        }
        return counter;
    }
};