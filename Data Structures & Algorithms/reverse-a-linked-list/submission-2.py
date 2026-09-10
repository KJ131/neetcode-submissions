# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        previous = None
        while curr:
            nxt = curr.next
            curr.next = previous
            previous = curr
            curr = nxt
        return previous

            

        
        