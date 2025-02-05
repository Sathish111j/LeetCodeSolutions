# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res=[[-1]*n for _ in range(m)]

        top,bottom=0,m-1
        left,right=0,n-1

        while head:
            for col in range(left,right+1):
                if not head : break
                res[top][col]=head.val
                head=head.next
            top+=1

            for row in range(top,bottom+1):
                if not head : break
                res[row][right]=head.val
                head=head.next
            right-=1

            for col in range(right,left-1,-1):
                if not head : break
                res[bottom][col]=head.val
                head=head.next
            bottom-=1
            
            for row in range(bottom,top-1,-1):
                if not head : break
                res[row][left]=head.val
                head=head.next
            left+=1

        return res
