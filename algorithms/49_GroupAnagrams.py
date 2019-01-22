class Solution:
    def groupAnagrams(self, strs):
        """
        Create a hashmap, then for every string sort them since all anagrams will be the same after sorting, then insert the string into the corresponding entry, and loop through the entire hashmap to get all group of anagrams. Best runtime 108ms beats 99%
        """
        dict = {}
        for str in strs:
            l = list(str)
            l.sort()
            l_t = tuple(l)
            if l_t in dict:
                dict[l_t].append(str)
            else:
                dict[l_t] = [str]
        return list(dict.values())