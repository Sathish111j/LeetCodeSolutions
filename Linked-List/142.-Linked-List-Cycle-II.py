# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        length=0

        while f and f.next:
            f=f.next.next
            s=s.next

            if s==f:
                while True:
                    s=s.next
                    length+=1
                    if s==f:
                        break
                break #break when cycler and lenght id found
                
        if length==0:
            return None



        left=head
        right=head

        while length>0:
            right=right.next
            length-=1

        while(right!=left):
            left=left.next
            right=right.next
        return right