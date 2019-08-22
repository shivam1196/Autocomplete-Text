class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self, suffix='', all_suffix=[]):
        current_node = self
        if current_node.is_word:
            all_suffix.append(suffix)
        for char in current_node.children:
            current_node.children[char].suffixes(suffix + char, all_suffix)
        return all_suffix

    def print_tree(self, suffix=''):
        current_node = self
        if current_node.is_word:
            print(suffix)
        for char in current_node.children:
            current_node.children[char].print_tree(suffix + char)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                current_node.children[i] = TrieNode()
            current_node = current_node.children[i]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node


def autocomplete(prefix):
    prefix_node = MyTrie.find(prefix)
    if prefix_node:
        print('\n'.join(prefix_node.suffixes()))
    else:
        print(prefix + " not found")


if __name__ == '__main__':
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in wordList:
        MyTrie.insert(word)

    pref = input('Enter Text ')
    if pref is not '':
        autocomplete(pref)
    else:
        print('Empty Prefix')

## Test case 1:
# Input Text an
# Output
    # t
    # thology
    # tagonist
    # tonym

## Test case 2:
# Input Text :
# Output
    # Empty Prefix

## Test case 3:
# Input Text f
# Output
    # un
    # unction
    # actory
