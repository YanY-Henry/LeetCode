# Add Two Numbers/两数相加

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_head = None

        ten = 0
        while l1 is not None or l2 is not None:         O(n) time
            n1 = l1.val if l1 != None else 0
            n2 = l2.val if l2 != None else 0

            tmp = n1 + n2 + ten
            one = tmp % 10
            ten = tmp // 10

            if answer_head == None:                     O(1) space
                answer_head = ListNode(val=one)
                answer_last = answer_head
            else:
                answer_last.next = ListNode(val=one)
                answer_last = answer_last.next

            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2

        # 最后还有一次可能的进位
        if ten != 0:
            answer_last.next = ListNode(val=ten)

        return answer_head