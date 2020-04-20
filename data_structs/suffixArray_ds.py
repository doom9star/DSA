class SuffixArray:
    def __init__(self, string):
        self.text = string
        self.substrings = 0
        self.length = len(string)
        self.lcpArray = [0]
        self.sortedSuffixArray = []
        self.colors = []
        self._manipulate()
        self._buildSuffixArray()
        self._buildLcpArray()

    def getTextLength(self):
        return self.length

    def getSuffixArray(self):
        return self.sortedSuffixArray

    def getLcpArray(self):
        return self.lcpArray

    def _manipulate(self):
        self.substrings = self.text.count(" ") + 1
        self.colors = [chr(ord("A") + index) for index in range(self.substrings)]
        self.text = self.text.replace(" ", "#")

    def _buildSuffixArray(self):
        suffixes = [self.text[index:] for index in range(self.length - 1, -1, -1)]
        suffixes = list(filter(lambda string: string[0] != "#", suffixes))
        self.sortedSuffixArray = sorted(suffixes)

    def _buildLcpArray(self):
        for index in range(1, len(self.sortedSuffixArray)):
            common_vals = 0
            first_counter = 0
            second_counter = 0
            while True:
                if (first_counter < len(self.sortedSuffixArray[index]) and second_counter < len(
                        self.sortedSuffixArray[index - 1])) and (
                        self.sortedSuffixArray[index][first_counter] == self.sortedSuffixArray[index - 1][
                    second_counter]):
                    common_vals += 1
                else:
                    self.lcpArray.append(common_vals)
                    break
                first_counter += 1
                second_counter += 1

    def longestCommonSubstring(self):
        if self.substrings > 1:
            # LCS Algorithum
            # Assuming atleast 3 strings with longest common substring
            colors_for_suffixes = {}
            color_tracker = {}
            text = self.text.split("#")

            # window variables
            window_coordinates = [0, 0]
            k = 3
            matches = set()
            match_length = 0

            for color in self.colors:
                color_tracker[color] = 0
            for suffix in self.sortedSuffixArray:
                for string in text:
                    if suffix.find("#") == -1:
                        if suffix[0:] in string:
                            colors_for_suffixes[suffix] = self.colors[text.index(string)]
                            break
                    else:
                        if suffix[:suffix.find("#")] in string:
                            colors_for_suffixes[suffix] = self.colors[text.index(string)]
                            break
            suffix_color_values = list(colors_for_suffixes.values())
            color_tracker[suffix_color_values[window_coordinates[0]]] += 1

            while window_coordinates[0] < len(self.sortedSuffixArray) - 2:
                difference = abs(window_coordinates[0] - window_coordinates[1])
                if difference < k - 1:
                    window_coordinates[1] += 1
                    color_tracker[suffix_color_values[window_coordinates[1]]] += 1
                elif difference > k - 1:
                    window_coordinates[0] += 1
                    color_tracker[suffix_color_values[window_coordinates[0]]] -= 1
                else:
                    summ = sum(color_tracker.values())
                    if summ == k:
                        match = self.sortedSuffixArray[window_coordinates[0]][
                                :self.sortedSuffixArray[window_coordinates[0]].find("#")]
                        if match in self.sortedSuffixArray[window_coordinates[0] + 1][
                                    :self.sortedSuffixArray[window_coordinates[0] + 1].find("#")] and match in \
                                self.sortedSuffixArray[window_coordinates[0] + 2][
                                :self.sortedSuffixArray[window_coordinates[0] + 2].find("#")]:
                            addition = []
                            for color in list(color_tracker.keys()):
                                for time in range(color_tracker[color]):
                                    addition.append(color)
                            if len(set(addition)) == 3:
                                if len(match) > match_length:
                                    matches.clear()
                                    matches.add(match)
                                    match_length = len(match)
                                elif len(match) == match_length:
                                    matches.add(match)
                                else:
                                    pass
                        if window_coordinates[1] < len(suffix_color_values) - 1:
                            window_coordinates[1] += 1
                            color_tracker[suffix_color_values[window_coordinates[1]]] += 1
                        else:
                            window_coordinates[0] += 1
                            color_tracker[suffix_color_values[window_coordinates[1]]] -= 1
            return matches
        else:
            print("There must be more than 1 word to find the longest common substring!")

    def longestRepeatedSubstring(self):
        suffix = self.getSuffixArray()[max(self.getLcpArray())]
        return suffix[:suffix.find("#")]


sa = SuffixArray("ABCA BCBA BCAC ACAB")
print(sa.getSuffixArray())
print(sa.getLcpArray())

# Longest Common Substring
print(sa.longestCommonSubstring())
print(sa.longestRepeatedSubstring())
