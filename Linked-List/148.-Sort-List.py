# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def find_middle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            dummy = ListNode()
            tail = dummy

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            if left:
                tail.next = left
            if right:
                tail.next = right

            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head

            middle = find_middle(head)
            right_head = middle.next
            middle.next = None

            left = merge_sort(head)
            right = merge_sort(right_head)

            return merge(left, right)

        return merge_sort(head)