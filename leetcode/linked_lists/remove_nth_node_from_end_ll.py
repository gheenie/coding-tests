from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count linked list length
        length = 1
        current_node = head
        while (current_node.next != None):
            current_node = current_node.next
            length += 1

        # Get the node before the removed element
        front_position = length - n - 1
        # Edge case
        if front_position == -1:
            # Where linked list is one element
            if length == 1: return None
            # Where removed element is the head
            return head.next
        current_node = head
        for _ in range(front_position):
            current_node = current_node.next

        # Reference the node after the removed element
        current_node.next = current_node.next.next

        current_node = head
        return current_node


solution = Solution()
one, two, three, four, five = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
one.next, two.next, three.next, four.next = two, three, four, five
print(solution.removeNthFromEnd(one, 2))
one = ListNode(1)
print(solution.removeNthFromEnd(one, 1))
