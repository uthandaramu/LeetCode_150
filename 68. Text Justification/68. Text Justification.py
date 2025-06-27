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

            # condition (len of each words with a space at end and the len of word to be added) > maxWidth
            if (line_length + len(line) + len(words[i])) > maxWidth:
                # Line completed (no room)
                # Let's distribute the spaces then
                spaces = maxWidth - (line_length)
                spacesBetween = spaces // max(1, len(line) - 1)
                extraSpace = spaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spacesBetween
                    if extraSpace:
                        line[j] += " "
                        extraSpace -= 1

                result.append("".join(line))
                line, line_length = [], 0

            # Line not complete
            line.append(words[i])
            line_length += len(words[i])
            i += 1

        # Handle Last Line
        last_line = (" ".join(line))
        trailingSpaces = maxWidth - (len(last_line))
        result.append(last_line + (" " * trailingSpaces))
        return result