class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            sortedString = ''.join(sorted(word))
            anagrams[sortedString].append(word)
        return list(anagrams.values())
