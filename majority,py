class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        a=len(nums)//2
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            if freq[i]>a:
                return i
            
        
        
