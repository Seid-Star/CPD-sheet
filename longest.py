class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            a=strs[0][i]
            for x in strs[1:]:
                if i>=len(x) or x[i]!=a:
                    return strs[0][:i]
        return strs[0]
