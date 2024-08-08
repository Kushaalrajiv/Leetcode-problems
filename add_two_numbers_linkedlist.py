class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        new_node = node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end="  ")
            current = current.next
        

    def sum(self, l2):
        carry = 0
        p1 = self.head
        p2 = l2.head
        result_list = linked_list()

        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            result_list.append(new_val)

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return result_list


input_list1 = [7]
input_list2 = [5]

linked_list1 = linked_list()
linked_list2 = linked_list()

for value in input_list1:
    linked_list1.append(value)

for value in input_list2:
    linked_list2.append(value)

result = linked_list1.sum(linked_list2)

print("Sum of linked lists:")
result.print_list()


# Using only nodes as per leetcode.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         new_sum = ListNode()
#         current = new_sum
#         carry = 0
        
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
            
#             total_value = v1 + v2 + carry
#             carry = total_value // 10
#             total = total_value % 10
            
#             current.next = ListNode(total)
#             current = current.next    
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
                
#         return new_sum.next
