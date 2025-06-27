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
                    mutantGene = gene[:idx] + letter + gene[idx + 1:]

                    if mutantGene in geneBank and mutantGene not in visited:
                        queue_box.append((level + 1, mutantGene))
                        visited.add(mutantGene)

        return -1