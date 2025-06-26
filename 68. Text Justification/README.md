### 68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

A word is defined as a character sequence consisting of non-space characters only.  
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.  
The input array words contains at least one word.  

**Example 1:**

**Input:** words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16  
**Output:**  
[   
   "This    is    an",  
   "example  of text",  
   "justification.  "  
]

**Example 2:**

**Input:** words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16  
**Output:**  
[  
  "What   must   be",  
  "acknowledgment  ",  
  "shall be        "  
]  
**Explanation:** Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.  
Note that the second line is also left-justified because it contains only one word.

**Example 3:**

**Input:** words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20  
**Output:**  
[  
  "Science  is  what we",  
  "understand      well",  
  "enough to explain to",  
  "a  computer.  Art is",  
  "everything  else  we",  
  "do                  "  
]  

**Constraints:**

* 1 <= words.length <= 300
* 1 <= words[i].length <= 20
* words[i] consists of only English letters and symbols.
* 1 <= maxWidth <= 100
* words[i].length <= maxWidth

```python
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        size = len(words)
        i = 0
        line, line_length = [], 0

        while (i < size):

            #condition (len of each words with a space at end and the len of word to be added) > maxWidth
            if (line_length + len(line) + len(words[i])) > maxWidth:
                #Line completed (no room)
                #Let's distribute the spaces then
                spaces = maxWidth - (line_length)
                spacesBetween = spaces // max(1, len(line)-1)
                extraSpace = spaces % max(1, len(line)-1)

                for j in range(max(1,len(line)-1)):
                    line[j] += " " * spacesBetween
                    if extraSpace:
                        line[j] += " "
                        extraSpace -= 1
                
                result.append("".join(line))
                line, line_length = [], 0

            #Line not complete
            line.append(words[i])
            line_length += len(words[i])
            i += 1
        
        #Handle Last Line      
        last_line = (" ".join(line))
        trailingSpaces = maxWidth - (len(last_line))
        result.append(last_line + (" " * trailingSpaces))
        return result
```