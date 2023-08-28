from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_linkedlist = []
        while headA != None:
            a_linkedlist.append(headA)
            headA = headA.next

        intersect_found = False
        while intersect_found == False or headB != None:
            if headB in a_linkedlist: intersect_found = True
            else: headB = headB.next

        return headB
