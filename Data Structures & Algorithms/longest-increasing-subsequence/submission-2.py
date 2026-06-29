class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails =[]
        n = len(nums)
        for num in nums:
            left = 0
            right = len(tails)-1
            while left<=right:
                mid = (left+right)//2
                if tails[mid]<num:
                    left = mid+1
                else:
                    right = mid-1
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails)