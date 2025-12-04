#PATTERN: 3 pointers one for prev, current, next
#         set next node, set current to point to prev
#         set prev to current
#         set current to next

#         ALL IN WHILE CURRENT loop

#COMPLEXITY: O(n) time to traverse, O(1) space for 3 pointers 

#TEMPLATE:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev