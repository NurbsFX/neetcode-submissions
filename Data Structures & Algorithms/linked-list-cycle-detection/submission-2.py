# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        
        l = head
        while l:
            if l not in seen: 
                seen.add(l)
                l = l.next
            else:
                return True
        return False