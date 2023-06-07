# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

class Trie:
    class Node(dict):
        def __init__(self, end=False, *args, **kwargs):
            self.end = end
            super().__init__(*args, **kwargs)
    
    def __init__(self):
        self.tree = self.Node()
    
    def get(self, key):
        node = self.tree
        for char in key:
            if char in node:
                node = node[char]
            else:
                raise KeyError(key)
                 
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


def autocomplete(query, strings):
    trie = Trie()
    for string in strings:
        trie.set(string)
    return list(trie.get(query))


print(autocomplete('de', ['dog', 'deer', 'deal'])) #=> ['deer', 'deal']