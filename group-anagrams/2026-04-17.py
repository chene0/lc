class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            grouped[key].append(s)

        return list(grouped.values())
