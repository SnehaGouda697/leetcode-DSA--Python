class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """set_conv1 = set(s)
        set_conv2 = set(t)
        st = set_conv1.issubset(set_conv2)
        return st
        """
        return sorted(s) == sorted(t)