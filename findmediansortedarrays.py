class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = []
        l1,l2 = len(nums1),len(nums2)
        if l1+l2 == 0:
    		return 0
        if (l1+l2)%2 != 0:
        	median = [(l1+l2)/2]
    	else:
    		median = [(l1+l2)/2,(l1+l2)/2-1]
		