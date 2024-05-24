# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = second = dummy

        # count (n+1)-th node from beginning (not end)
        for _ in range(n + 1):
            first = first.next

        # when 'first' reaches the end, second will have traversed to (n+1)-th node from the end, ie one node BEFORE the n-th node from the end
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next # skip/delete node
        return dummy.next
