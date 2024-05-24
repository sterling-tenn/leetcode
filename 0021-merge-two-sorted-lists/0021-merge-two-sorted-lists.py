# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy to start the linked list
        curr = dummy # start to build from the dummy by manipulating node next pointers
        
        # list1 and list2 serve as traversal pointers
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next # traverse
            else:
                curr.next = list2
                list2 = list2.next # traverse

            curr = curr.next
        
        # case where length of lists are not equal
        while list1 or list2:
            if list1:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
                
            curr = curr.next
        
        return dummy.next # since root dummy was just to start building the LL
                