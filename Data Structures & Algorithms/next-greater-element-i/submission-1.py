class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n2 = len(nums2)
        nge={}
        for i in range(n2):
            print("stack ",stack)
            print("nge ",nge)
            while stack and nums2[i]>nums2[stack[-1]]:
                nge[nums2[stack.pop()]] = nums2[i]
            stack.append(i)

        while stack:
            nge[nums2[stack.pop()]]=-1
        print(nge)
        res=[]
        for x in nums1:
            print(x, nge[x])
            res.append(nge[x])
        return( res)