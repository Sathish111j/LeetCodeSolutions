# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
            
        slow,fast=head,head.next

        # finding the middle element

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev,current=None,slow.next
        slow.next=None

        # reversing the second list 

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        first,second=head,prev

        # merging two ll
        while second:
            temp1,temp2=first.next,second.next

            first.next=second
            second.next=temp1

            first,second=temp1,temp2
        
    