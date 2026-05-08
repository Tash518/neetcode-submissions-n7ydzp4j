class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r= 0,n-1
        if nums[l]<nums[r]:
            while l<=r:
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        print(f'{l}:{nums[l]}, target: {target}')
        if nums[l]==target:
            return l
        if nums[l]<=target<=nums[n-1]:
            print(f'{l}:{nums[l]}, target: {target}')
            print(" nums[l] < target < nums[n-1] ")
            low = l+1
            high = n-1
            while low<=high:
                mid = (low+high)//2
                if target == nums[mid]:
                    return mid
                elif target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        else:
            low = 0
            high = l-1
            while low<=high:
                mid = (low+high)//2
                if target == nums[mid]:
                    return mid
                elif target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return -1
