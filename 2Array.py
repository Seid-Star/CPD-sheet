class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2:
                if i not in arr:
                    c=nums1.count(i)
                    d=nums2.count(i)
                    for y in range(min(c,d)):
                        arr.append(i)
        return arr
        
