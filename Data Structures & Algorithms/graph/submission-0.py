class Graph:
    
    def __init__(self):
        self.adjency_list ={}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjency_list:
            self.adjency_list[src] = []
        if dst not in self.adjency_list:
            self.adjency_list[dst] = []
        self.adjency_list[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjency_list or dst not in self.adjency_list:
            return False
        
        for node in self.adjency_list[src]:
            if node == dst:
                self.adjency_list[src].remove(dst)
                return True

        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        visited.add(src)
        queue = deque()
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                if current == dst:
                    return True
                
                for neighbor in self.adjency_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return False


