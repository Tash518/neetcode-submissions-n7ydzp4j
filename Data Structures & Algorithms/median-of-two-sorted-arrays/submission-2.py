class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        MIN = float('-inf')
        MAX = float('inf')
        m,n = len(nums1),len(nums2)
        
        if m>n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        
        low,high = 0,m
        leftpartsize = (m+n+1)//2
        while low<=high:

            cut1 = (low+high)//2
            cut2 = leftpartsize - cut1

            left1 =MIN if cut1==0 else nums1[cut1-1]
            left2 =MIN if cut2==0 else nums2[cut2-1]

            right1 = MAX if cut1==m else nums1[cut1]
            right2 = MAX if cut2==n else nums2[cut2]

            if left1<=right2 and left2<=right1:

                if (m+n)%2 != 0:
                    return max(left1,left2)
                
                return (max(left1,left2)+min(right1,right2))/2
            
            elif left1>right2:
                high = cut1-1
            else:
                low = cut1+1
                

        

        