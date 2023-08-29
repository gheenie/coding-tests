from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if head == None: return None

        # Variable to store traversed nodes
        linkedlist = []
        # Store the first node and start from the next
        linkedlist.append(head)
        head = head.next

        # While the next node is not in the list of traversed nodes
        # and a cycle does exist
        while head not in linkedlist and head != None:
            linkedlist.append(head)
            head = head.next
        
        # While loop will exit with head pointing at the recycled node
        # or the None tail
        return head