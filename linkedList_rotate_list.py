# Question:
# Given the head of a linked list, 
# rotate the list to the right by k places.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int) :

        if head == None or head.next == None :
            return head

        # list ka length aur last node
        last = head
        l = 0

        while last.next != None :
            last = last.next
            l += 1
        # last node k lye
        l += 1

        # agr k list k len k equal h to len ko k se % kr k jo bachega utna bar hi rotate krna hoga
        # optimize k
        k %= l

        if k == 0 :
            return head
        
         # find new tail
        curr = head

        # this finds the node just before the new head.
        for _ in range(l - k - 1) :
            curr = curr.next
        
        # rotate
        last.next = head
        head = curr.next
        curr.next = None

        return head
    
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

def print_linked_list(head) :
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

arr = [0,1,2]
k = 4
        
head = build_list(arr)

print("Original:")
print_linked_list(head)

sol = Solution()
head = sol.rotateRight(head, k)
print("After rotating:")
print_linked_list(head)


        