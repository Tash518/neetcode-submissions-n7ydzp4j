from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()#only indices
        ans=[]
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:#remove out of window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:#maintain decreasing order
                dq.pop()
            dq.append(i)

            if i>=k-1:
                ans.append(nums[dq[0]]) #add max to answer
        return ans