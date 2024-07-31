# Anagram Groups

# Medium

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# In O(n)

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()



# In O(n^2) (technically O(n^2 * string_length))

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        lst = []
        def make_dic(str):
            new_dic = {}
            for i in str:
                if i not in new_dic:
                    new_dic[i] = 1
                else:
                    new_dic[i] += 1
            return new_dic
        
        for word in strs:
            lst.append(make_dic(word))
        
        new_lst = []
        seen = set()
        
        for a in range(len(lst)):
            if a not in seen:
                group = [strs[a]]
                for z in range(a + 1, len(lst)):
                    if lst[a] == lst[z]:
                        group.append(strs[z])
                        seen.add(z)
                if len(group) >= 1:
                    new_lst.append(group)
                
        return new_lst

    
    
