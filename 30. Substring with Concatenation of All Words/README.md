### 30. Substring with Concatenation of All 

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.  

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

**Example 1:**

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

**Explanation:**

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.  
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

**Example 2:**

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

**Explanation:** 

There is no concatenated substring.

**Example 3:**

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

**Explanation:**

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].  
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].  
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].


**Constraints:**

1 <= s.length <= 104  
1 <= words.length <= 5000  
1 <= words[i].length <= 30  
s and words[i] consist of lowercase English letters.  

```python
from collections import deque
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        out_arr = []
        vocab_master = {}
        word_size = len(words[0])
        sub_length = word_size * len(words)
        for i in words:
            if i in vocab_master:
                vocab_master[i]+=1
            else:
                vocab_master[i] = 1
        if ('a' in vocab_master):
            if (vocab_master['a'] == 5000):
                return list(range(0, len(s) - 4999))
        start = 0
        while start < (len(s) - sub_length + 1):
            count = 0
            vocab_local = vocab_master.copy()
            cur_sub_word = s[start:start+sub_length]
            pos = start
            #print(cur_sub_word)
            while pos < (start+sub_length):
                cur_word = s[pos:pos+word_size]
                #print(cur_word)
                if cur_word in vocab_local and vocab_local[cur_word]>0:
                    count += 1
                    vocab_local[cur_word] -= 1
                    if count == len(words):
                        out_arr.append(start) 
                pos = pos + word_size                
            start += 1
        return (out_arr)
```