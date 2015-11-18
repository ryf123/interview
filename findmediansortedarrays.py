class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        if l1+l2 == 0:
            return None
        if (l1+l2)%2 == 0:
            return (self.kthelement((l1+l2)/2,0,0,l1,l2)+self.kthelement((l1+l2)/2+1,0,0,l1,l2))*0.5
        else:
            return self.kthelement((l1+l2)/2+1,0,0,l1,l2)

    def kthelement(self,k,start1,start2,l1,l2):
        # print k,start1,start2,l1,l2
        if l1 == 0:
            return self.nums2[start2+k-1]
        elif l2 == 0:
            return self.nums1[start1+k-1]
        if k == 1:
            return min(self.nums1[start1],self.nums2[start2])
        pa = min(k/2,l1)
        pb = min(k/2,l2)
        if self.nums1[start1+pa-1] <= self.nums2[start2+pb-1]:
            return self.kthelement(k-pa,start1+pa,start2,l1-pa,l2)
        else:
            return self.kthelement(k-pb,start1,start2+pb,l1,l2-pb)
s = Solution()
num1,num2 = [1,2,3,4],[5,6,7,8]
# num1,num2 = [1,2],[1,1]
# num1,num2 = [1],[2,3,4,5,6]
num1,num2 = [],[1,2,3,4,5]
print s.findMedianSortedArrays(num1,num2)