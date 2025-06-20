### 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

There is no string in strs that can be rearranged to form "bat".  
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.  
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.  

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**Constraints:**

* 1 <= strs.length <= 104
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hash_dict:
                hash_dict[sorted_word] = [word]
            else:
                hash_dict[sorted_word].append(word)
        
        out = []

        for i in hash_dict.values():
            out.append(i)
        
        return (out)
```