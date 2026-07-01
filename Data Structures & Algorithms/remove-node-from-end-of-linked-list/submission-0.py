# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        # temp2 = None
        length = 0
        while temp:
            length += 1
            # temp2 = temp
            temp = temp.next
        
        target = length - n + 1

        if target == 1:
            a = head
            head = head.next

        
        elif target == length:
            temp = head
            c = 1
            while c < target - 1:
                temp = temp.next
                c += 1
            temp.next = None
        
        else:
            c = 1
            prev = None
            curr = head
            while c < target:
                prev = curr
                curr = curr.next
                c += 1
            
            prev.next = curr.next
            curr.next = None

        return head


                