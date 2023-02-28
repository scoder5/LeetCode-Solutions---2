from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = defaultdict(list)
        for i in strs:
            letters[tuple(sorted(i))].append(i)
        return list(letters.values())