class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, currentLine, currentLineLength = [], [], 0

        for word in words:
            # Length of words + length of new word + number of spaces+1 > maxWidth means we can't fit the next word here so add spaces
            if currentLineLength + len(word) + len(currentLine) > maxWidth:
                for i in range(maxWidth - currentLineLength):
                    # Add space after each word in currentLine.
                    currentLine[i % (
                                len(currentLine) - 1 or 1)] += ' '  # The "or 1" is to handle the case where there's only one word in the line
                result.append(''.join(currentLine))
                currentLine, currentLineLength = [], 0
            currentLine.append(word)
            currentLineLength += len(word)

        result.append(' '.join(currentLine).ljust(maxWidth,
                                                  ' '))  # can also do + " "*(maxWidth - len(' '.join(currentLine))) instead of .ljust

        return result