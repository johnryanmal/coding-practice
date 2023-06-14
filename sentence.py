# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

class Trie:
    class Node(dict):
        def __init__(self, end=False, *args, **kwargs):
            self.end = end
            super().__init__(*args, **kwargs)
    
    def __init__(self, keys):
        self.tree = self.Node()
        for key in keys:
            self.set(key)
    
    def get(self, key):
        node = self.tree
        for char in key:
            if char in node:
                node = node[char]
            else:
                return
                 
        def dfs(node):
            if node.end:
                yield ''
            
            for key, child in node.items():
                yield from (key+value for value in dfs(child))
        
        yield from (key+value for value in dfs(node))

    def set(self, key):
        node = self.tree
        for char in key:
            if char not in node:
                node[char] = self.Node()
            node = node[char]
        node.end = True


def sentence(string, words):
    trie = Trie(words)
    length = len(string)

    def dfs(i):
        if i == length:
            return []
        if i > length:
            return None
        
        for word in trie.get(string[i]):
            if string[i:].startswith(word):
                result = dfs(i + len(word))
                if result is not None:
                    return [word] + result

    return dfs(0)


print(sentence('thequickbrownfox',['the','quick','brown','fox'])) #=> ['the','quick','brown','fox']
print(sentence('bedbathandbeyond',['bed','bath','bedbath','and','beyond'])) #=> ['bed','bath','and','beyond']
print(sentence('bedbathandbeyond',['bed','bath','an','db','bat','hand','beyond'])) #=> ['bed','bat','hand','beyond']