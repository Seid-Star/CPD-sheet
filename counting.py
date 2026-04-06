class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        a=0
        count=0
        while a<len(nums):
            for i in range(len(nums)):
                if abs(nums[a]-nums[i])==k:
                    count+=1
            a+=1
        return count//2
