from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Parse the linked lists into lists
        a_linkedlist = []
        b_linkedlist = []
        while headA != None:
            a_linkedlist.append(headA)
            headA = headA.next
        while headB != None:
            b_linkedlist.append(headB)
            headB = headB.next

        # Reverse the lists to traverse from back to front
        a_linkedlist.reverse()
        b_linkedlist.reverse()

        # Assign the lists according to their length
        shorter_linkedlist = a_linkedlist
        longer_linkedlist = b_linkedlist
        if len(b_linkedlist) < len(a_linkedlist):
            shorter_linkedlist = b_linkedlist
            longer_linkedlist = a_linkedlist

        # Edge cases
        # First (from the back) node is already not the same
        if shorter_linkedlist[0] != longer_linkedlist[0]:
            return None
        # Either lists only have 1 node and they intersect
        elif len(a_linkedlist) == 1 or len(b_linkedlist) == 1:
            return a_linkedlist[0]

        # Traverse both lists at the same time
        for i, node in enumerate(shorter_linkedlist):
            if node != longer_linkedlist[i]:
                return shorter_linkedlist[i - 1]

        # Both original linked lists intersected right from the start
        return shorter_linkedlist[-1]
