from typing import Optional, Union, List

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, 
        l1: Union[ListNode, List[int], None], 
        l2: Union[ListNode, List[int], None]
    ) -> List[int]:
        
        # 1. Helper function to convert a Python list into a ListNode chain
        def to_linked_list(data):
            if isinstance(data, list):
                dummy = ListNode()
                curr = dummy
                for val in data:
                    curr.next = ListNode(val)
                    curr = curr.next
                return dummy.next
            return data

        # Automatically convert l1 and l2 if passed as Python lists
        l1 = to_linked_list(l1)
        l2 = to_linked_list(l2)

        # 2. Main Addition Logic
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            
            total = value1 + value2 + carry
            carry = total // 10
            value = total % 10
            
            current.next = ListNode(value)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # 3. Convert result back to a standard Python list
        result = []
        curr = dummy.next
        while curr:
            result.append(curr.val)
            curr = curr.next
            
        return result


solution = Solution()
print(solution.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
