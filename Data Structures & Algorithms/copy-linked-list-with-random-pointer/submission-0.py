"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        '''while(temp):
            print(temp.val, end=" ")
            temp=temp.next'''
        print()
        randmap = {}
        cur = Node(x=head.val)
        randmap[head] = cur
        ans = cur
        head = head.next
        while head:
            cur.next = Node(head.val)
            cur = cur.next
            randmap[head] = cur
            head = head.next
        temp = ans
        '''while(temp):
            print(temp.val, end=" ")
            temp=temp.next'''
        print()
        for k,v in randmap.items():
            #print(f'key:{k.val} value:{v.val}, k.random  = {k.random.val if k.random else None}')
            v.random = randmap.get(k.random)
        return ans
            
            
        
            

