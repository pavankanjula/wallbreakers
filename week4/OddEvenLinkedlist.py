# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Time - O(n)
        # Space - O(1)
        # handling edge cases
        if head is None or head.next is None or head.next.next is None:
            return head
        odd = head  # odd head
        even = head.next  # even head
        evenptr = head.next  # remembers the head of even start node
        while even.next and even.next.next:
            # connecting odd to next odd
            odd.next = even.next
            odd = odd.next
            # connecting even to next even
            even.next = odd.next
            even = even.next
        if even.next:  # if one extra node is there, connect it to odd.
            odd.next = even.next
            even.next = None
            odd = odd.next
        odd.next = evenptr
        return head
