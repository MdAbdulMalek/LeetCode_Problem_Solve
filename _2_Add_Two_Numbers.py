class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)-> ListNode:
        num1 = ''
        while l1 :
            num1 = str(l1.val)  + num1  
            l1 = l1.next
        num2 = ''
        while l2 :
            num2 = str(l2.val)  + num2  
            l2 = l2.next
            
        nums_sum = str(int(num1) + int(num2))

        reverse_node = ListNode(val = nums_sum[-1])
        nums_sum = nums_sum[:-1]
        temp = reverse_node
        while nums_sum:
            new_node = ListNode(val = nums_sum[-1])
            temp.next = new_node
            temp = temp.next 
            nums_sum = nums_sum[:-1]
            
        return reverse_node
