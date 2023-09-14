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
    ListNode *detectCycle(ListNode *head) {
        ListNode* slowPtr = head;
        ListNode* fastPtr = head;
        
        while(fastPtr && fastPtr->next){
            slowPtr = slowPtr->next;
            fastPtr = fastPtr->next->next;
            if(slowPtr == fastPtr) break;
        }
        
        if(!(fastPtr && fastPtr->next)) return NULL; // No cycle
        
        // There is a cycle
        while (true) {
            if(head == slowPtr) return head;
            head = head->next;
            slowPtr = slowPtr->next;
        }
    }
//     ========== EXPLANATION ==========
//     [definition #1] let x be distance travelled before the cycle
//     [definition #2] let y be the distance travelled into the cycle (from the start of the cycle)
//     slowPtr = x+y
//     fastPtr = 2(x+y)
        
//     therefore length of the cycle is some multiple (n) of fastPtr-slowPtr: nC = 2(x+y) - (x+y) = x+y
//     we have the position where slowPtr and fastPtr meet (at point y), so because nC = x+y, we know we must travel x distance from y to get back to the start of the cycle
//     which is the same distance the head is from the start of the cycle, so traverse head and location at y at the same rate until they're equal - the start of the cycle location
};