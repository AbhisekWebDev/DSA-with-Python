# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, head1, head2) :

        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        carry = 0
        curr3 = ans

        while curr1 != None or curr2 != None :
            total = carry
            carry = 0

            if curr1 != None :
                total += curr1.val
                curr1 = curr1.next
            
            if curr2 != None :
                total += curr2.val
                curr2 = curr2.next
            
            if total >= 10 :
                carry = 1
                total -= 10
            
            newNode = ListNode(total)
            curr3.next = newNode
            curr3 = curr3.next
        
        if carry > 0 :
            newNode = ListNode(carry)
            curr3.next = newNode
        
        return ans.next
        
def build_list(arr):
    head = None
    curr = None
    for val in arr:
        if not head:
            head = ListNode(val)
            curr = head
        else:
            curr.next = ListNode(val)
            curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Input: 342 + 465 = 807
l1 = build_list([2, 4, 3])
l2 = build_list([5, 6, 4])

print("List1:")
print_list(l1)

print("List2:")
print_list(l2)

sol = Solution()
res = sol.addTwoNumbers(l1, l2)

print("Sum:")
print_list(res)
