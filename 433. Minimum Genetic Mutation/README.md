### 433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.  

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

**Example 1:**

**Input:** startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
**Output:** 1

**Example 2:**

**Input:** startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]  
**Output:** 2

**Constraints:**

* 0 <= bank.length <= 10
* startGene.length == endGene.length == bank[i].length == 8
* startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


```python
from collections import defaultdict, deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        geneBank = defaultdict(int)

        for i, gene in enumerate(bank):
            geneBank[gene] = i

        if endGene not in geneBank:
            return -1
        
        queue_box = deque()
        queue_box.append((0, startGene))

        visited = set()

        while queue_box:
            level, gene = queue_box.popleft()

            if gene == endGene:
                return level

            for idx in range(8):
                for letter in ['A', 'C', 'G', 'T']:
                    mutantGene = gene[:idx] + letter + gene[idx+1:]

                    if mutantGene in geneBank and mutantGene not in visited:
                        queue_box.append((level + 1, mutantGene))
                        visited.add(mutantGene)
                    
        return -1
```