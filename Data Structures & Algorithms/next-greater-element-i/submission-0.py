class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge=[-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                nge[stack.pop()] = nums2[i]
            stack.append(i)
        print(nge)
        res=[]
        for x in nums1:
            for i in range(len(nums2)):
                if nums2[i]==x:
                    res.append(nge[i])
        return( res)