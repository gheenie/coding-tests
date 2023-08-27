from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Strings to store linked list traversed values
        l1_string = ''
        l2_string = ''

        # Traverse each linked list and build the strings from back to front
        while l1 != None:
            l1_string = str(l1.val) + l1_string
            l1 = l1.next
        while l2 != None:
            l2_string = str(l2.val) + l2_string
            l2 = l2.next

        sum_string = str(int(l1_string) + int(l2_string))

        # Initialise the head node for a new linked list
        sum_linkedlist = ListNode(sum_string[-1])
        # Store a pointer to the head node for returning
        head_sum_linkedlist = sum_linkedlist

        # Build the linked list from the sum's digits, back to front
        for i in range(len(sum_string) - 1, 0, -1):
            sum_linkedlist.next = ListNode(sum_string[i - 1])
            sum_linkedlist = sum_linkedlist.next

        # Set the last node's next to None as this isn't done in the previous for loop 
        sum_linkedlist.next = None

        return head_sum_linkedlist
