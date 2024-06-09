# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        
        last.next=None
        k = k % length
        if k == 0:
            return head
        skip=length - k - 1

        new_last = head
        for _ in range(skip):
            new_last = new_last.next

        new_head = new_last.next
        new_last.next = None

        last.next = head
        
        return new_head

