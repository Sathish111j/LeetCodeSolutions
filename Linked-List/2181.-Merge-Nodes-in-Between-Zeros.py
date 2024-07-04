# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current =head.next
        sumval=0
        result = head 
        while current:
            if current.val==0:
                head.val=sumval
                if current.next:  
                    head = head.next
                sumval=0

            sumval+=current.val
            current=current.next
        head.next=None

        return result

