from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Variables to append nodes to after comparing values with x
        less_than_x = []
        more_than_equal_to_x = []

        # Variable to track traversal
        current_node = head
        
        # Traverse the linked list
        while current_node != None:
            # Sort the node into the appropriate list
            if current_node.val < x:
                less_than_x.append(current_node)
            else:
                more_than_equal_to_x.append(current_node)

            current_node = current_node.next

        # Set the next node for all elements with values < x
        for i in range(len(less_than_x) - 1):
            less_than_x[i].next = less_than_x[i + 1]

        # Set the next node for all elements with values >= x
        for i in range(len(more_than_equal_to_x) - 1):
            more_than_equal_to_x[i].next = more_than_equal_to_x[i + 1]
        
        # Just return head if either list is empty as the order is unchanged
        if len(less_than_x) == 0 or len(more_than_equal_to_x) == 0:
            return head
        else:
            # Link the two lists and set the last node's next to None
            less_than_x[-1].next = more_than_equal_to_x[0]
            more_than_equal_to_x[-1].next = None
            return less_than_x[0]
