```python
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create a graph to store the relationship between characters
        graph = defaultdict(list)
        
        # create a set to store all the characters
        chars = set()
        
        # iterate over the words and add the relationships to the graph
        for i in range(len(words)):
            for char in words[i]:
                chars.add(char)
            
            for j in range(i+1, len(words)):
                for k in range(min(len(words[i]), len(words[j]))):
                    if words[i][k] != words[j][k]:
                        graph[words[i][k]].append(words[j][k])
                        break
        
        # create a set to store the visited characters
        visited = set()
        
        # create a stack to store the topological order
        stack = []
        
        # iterate over the characters and perform topological sort
        for char in chars:
            if self.dfs(char, graph, visited, stack):
                return ""
        
        return ''.join(stack)
    
    def dfs(self, char, graph, visited, stack):
        if char in visited:
            return False
        
        visited.add(char)
        
        for neighbor in graph[char]:
            if self.dfs(neighbor, graph, visited, stack):
                return True
        
        stack.append(char)
        return False
```