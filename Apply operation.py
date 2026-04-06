class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
        a=nums.count(0)
        arr=[]
        for i in nums:
            if i!=0:
                arr.append(i)
        for x in range(a):
            arr.append(0) 
        return arr      
