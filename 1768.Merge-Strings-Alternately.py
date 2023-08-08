class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        for char1, char2 in itertools.zip_longest(word1, word2, fillvalue=""):
            output.append(char1)
            output.append(char2)
        return "".join(output)
