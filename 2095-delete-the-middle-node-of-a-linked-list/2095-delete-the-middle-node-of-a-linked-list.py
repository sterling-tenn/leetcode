# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        target_index = self.getLength(head)/2
        curr_index = 0
        
        curr = head
        prev = None
        while curr:
            if curr_index == target_index:
                if prev:
                    prev.next = curr.next
                else: # edge case when LL size is 1
                    head = curr.next
                break
                
            prev = curr
            curr = curr.next
            curr_index += 1
            
        return head
                
        
    def getLength(self, head):
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        return cnt