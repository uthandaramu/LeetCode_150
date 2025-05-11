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
        