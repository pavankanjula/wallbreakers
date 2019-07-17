# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Time - O(n) ; n is length of linkedlist
        #Space - O(1)
        if head is None or head.next is None: #handling edge cases.
            return head
        #Intiate variables cur, prev, next to store the 3 nodes temporarily which we are working on currently.
        cur = head.next
        prev = head
        prev.next = None
        next = cur.next
        while not next is None:
            cur.next = prev #reversing the link
            #Then slide the variables one one position right.
            prev = cur
            cur = next
            next = next.next
        cur.next = prev #Finally after traversing the linkedlist, reverse the last link
        return cur