# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.getIntfromLinknode(l1)
        n2 = self.getIntfromLinknode(l2)
        n3 = n1 + n2
        linknode_str = str(n3)[::-1]
        l3 = ListNode()
        now = ListNode()
        l3.next = now
        Next = ListNode()
        max = len(linknode_str)
        j = 1
        for i in linknode_str:
            now.val = int(i)
            if j == max:
                break
            now.next = Next
            now = Next
            Next = ListNode()
            j = j + 1
        return l3.next

    def getIntfromLinknode(self, l):
        str_num = ''
        while 1:
            str_num = str_num + str(l.val)
            if l.next == None:
                break
            l = l.next
        str_num = str_num[::-1] 
        return int(str_num)

l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1.next.val = 3
l2= l1
a = Solution()
print(a.addTwoNumbers(l1,l2).val,a.addTwoNumbers(l1,l2).next.val )