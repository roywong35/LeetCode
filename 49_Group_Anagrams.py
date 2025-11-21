from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    group = defaultdict(list)
    for x in strs:
        key = "".join(sorted(x))
        group[key].append(x)
    return list(group.values())

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))