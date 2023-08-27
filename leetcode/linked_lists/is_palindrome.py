from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Extract linked list values into a list
        digits = []
        while head != None:
            digits.append(head.val)
            head = head.next

        # Make a shallow copy and reverse it
        reversed_digits = [*digits]
        reversed_digits.reverse()

        return digits == reversed_digits
