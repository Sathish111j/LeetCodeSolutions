# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head=list1
        curr=list1
        i=0
        while i!=b+1:
            if i==a-1:
                nodeA=curr
            if i==b:
                nodeB=curr.next
            i+=1
            curr=curr.next
        
        nodeA.next=list2
        curr2=list2

        while curr2.next:
            curr2=curr2.next
        
        curr2.next=nodeB

        return head
        

