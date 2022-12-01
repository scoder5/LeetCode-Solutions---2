class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_values(s):
            count = 0
            vowels = "aeiouAEIOU"
            for i in s:
                if i in vowels:
                    count += 1
            return count
        
        return count_values(s[:len(s)//2]) == count_values(s[len(s)//2:])