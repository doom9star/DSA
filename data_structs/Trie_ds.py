class Trie:
    def __init__(self):
        self.main = {}
        self.words = 0

    def add(self, word):
        curPos = self.main
        for char in word.lower():
            if char not in curPos:
                curPos[char] = {}
            curPos = curPos[char]
        curPos['*'] = True
        self.words += 1

    def total_words(self):
        print(self.words)

    def includes(self, word):
        curPos = self.main
        for ch in word:
            if ch not in curPos:
                print(False)
                return
            curPos = curPos[ch]
        print(True)

    def display(self):
        pass

    def delete(self, word):
        curPos = self.main
        prevPos = None
        prev_ch = None
        for ch in word:
            if ch not in curPos:
                print("Student Not Found!")
                return
            if len(curPos) > 1:
                prevPos = curPos
                curPos = curPos[ch]
                prev_ch = ch
            else:
                del prevPos[prev_ch]
                break


students = ['john', 'jacob', 'Jacky', 'doug', 'harry', 'karthik']
My_trie = Trie()
for student in students:
    My_trie.add(student)
# My_trie.total_words()
# My_trie.includes('karthik')
My_trie.delete('karthik')
My_trie.display()
