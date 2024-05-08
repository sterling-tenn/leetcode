# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        
        # Put all nodes in a stack so we can get reverse order
        while curr:
            stack.append(curr)
            curr = curr.next
            
        curr = head
        
        # Half of the nodes from the top of the stack get inserted into alternating positions
        for i in range(len(stack)/2):
            node = stack.pop()
            node.next = curr.next
            curr.next = node
            
            curr = curr.next.next # Every other node
            
        curr.next = None # end the list (we never removed the inserted reordered nodes)