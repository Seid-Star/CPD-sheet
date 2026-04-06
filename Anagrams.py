class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(p)
        arr=[]
        b=sorted(p)
        for i in range(len(s)-a+1):
            if b==sorted(s[i:i+a]):
                arr.append(i)
        return arr
