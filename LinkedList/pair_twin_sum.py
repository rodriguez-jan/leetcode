# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find_middle
        def find_middle(head):
            slow_ptr = head
            fast_ptr=head
            while(fast_ptr):
                slow_ptr = slow_ptr.next
                fast_ptr= fast_ptr.next.next
            return slow_ptr
        #reverse_list
        def reverse(middle):
            prev = None
            nxt = None
            curr = middle
            while(curr):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        #find_max
        def pair_sum(head):
            curr = head
            middle = find_middle(head)
            reverse_ptr = reverse(middle)
            max_sum = 0
            while(curr != middle):
                max_sum = max(max_sum,curr.val+reverse_ptr.val)
                curr = curr.next
                reverse_ptr = reverse_ptr.next
            return max_sum

        return pair_sum(head)

# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next