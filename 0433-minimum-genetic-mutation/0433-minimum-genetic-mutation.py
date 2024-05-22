class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        #build graph
        graph = {startGene : []} # graph initially has 1 node and no neighbors

        # all possible genes are nodes
        for gene in bank:
            if gene not in graph.keys():
                graph[gene] = []
        
        for node in graph: # for each node               
            for gene in bank: # find all its neighbors and add them
                if self.isValidMutation(node, gene):
                    graph[node].append(gene)

        return self.bfs(graph, startGene, endGene)
    
    # bfs search until target is found
    def bfs(self, graph, start, target):
        queue = [(start, 0)]
        visited = {start}
        
        while queue:
            node, distance = queue.pop(0)
            
            if node == target:
                return distance

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append( (neighbor, distance + 1) )
                    visited.add(neighbor)
                    
        return -1 # not found
            
        
    # check if two genes differ by only 1 character
    def isValidMutation(self, g1, g2):
        num_diff = 0
        
        for i in range(len(g1)):
            if g1[i] != g2[i]:
                num_diff += 1
                
        return num_diff == 1