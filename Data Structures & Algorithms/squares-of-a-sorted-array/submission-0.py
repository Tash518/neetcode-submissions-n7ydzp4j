class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1
        pos=right
        res=[0]*(right+1)
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res[pos]=nums[left]*nums[left]
                left+=1
                pos-=1
            else:
                res[pos]=nums[right]*nums[right]
                right-=1
                pos-=1
        return res
