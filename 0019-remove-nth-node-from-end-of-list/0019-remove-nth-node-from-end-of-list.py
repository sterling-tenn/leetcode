# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.getLength(head)
        cnt = 0
        curr = head
        prev = None
        while curr is not None:
            cnt += 1
            if cnt == length - n + 1:
                if prev is not None:
                    prev.next = curr.next
                else: # edge case if size of LL is 1
                    head = curr.next
                break
                
            prev = curr
            curr = curr.next
            
        return head
        
    def getLength(self, head):
        cnt = 0
        curr = head
        while curr is not None:
            cnt += 1
            curr = curr.next
            
        return cnt