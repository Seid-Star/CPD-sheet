class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2:
                if i not in arr:
                    arr.append(i)
        return arr
