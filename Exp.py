#1. Factorial:
num = int(input("Enter a number: "))

def fact(num):
    factorial = 1
    for i in range (1, num+1):
        factorial *= i
    return factorial

print("Factorial of ",num,": ", fact(num))

------------------------------------------------------------------------------------------------------------------------

#2. Length of a list
list = input("Enter a list separated by space: ").split()
num_list = [int (x) for x in list]
length = len(num_list)
print("Number of elements in the list are: ", length)

------------------------------------------------------------------------------------------------------------------------

#3. Reverse a list
def reversed_list(list):
    return list[::-1]

list = [1,2,3,4]
#list.reverse()
print("Reversed list: ", reversed_list(list))

------------------------------------------------------------------------------------------------------------------------

#4. DFS
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_edges(self, source, destination):
        self.adjacency_list.setdefault(source, []).append(destination)
        
    def dfs (self, start_node):
        visited = set()
        
        def dfs_helper(node):
            visited.add(node)
            
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)
                    
        dfs_helper(start_node)
        return visited
    
if __name__ == "__main__":
    graph = Graph()
    edges = int(input("Enter the number of edges: "))
    for i in range (edges):
        source, destination = map(int, input(f"Enter edge{i+1} (source, destination): ").split())
        graph.add_edges(source, destination)

start_node = int(input("Enter the starting node for traversal: "))
visited_nodes_dfs = graph.dfs(start_node)
print("DFS visited nodes: ", visited_nodes_dfs)

------------------------------------------------------------------------------------------------------------------------

#5. BFS
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_edges(self, source, destination):
        self.adjacency_list.setdefault(source, []).append(destination)
        
    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        
        while queue:
            node = queue.pop(0)
            visited.add(node)
            
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
        return visited
                
if __name__ == "__main__":
    graph = Graph()
    edges = int(input("Enter the number of edges: "))
    for i in range (edges):
        source, destination = map(int, input(f"Enter edge{i+1} (source, destination): ").split())
        graph.add_edges(source, destination)

start_node = int(input("Enter the starting node for traversal: "))
visited_nodes_bfs = graph.bfs(start_node)
print("BFS visited nodes: ", visited_nodes_bfs)

------------------------------------------------------------------------------------------------------------------------

#6. Water Jug using BFS    
from collections import deque

def bfs_solve_water_jug(cap1, cap2, goal):
    queue = deque([(0,0,[])])
    visited = {(0,0)}
    
    while queue:
        jug1, jug2, path = queue.popleft()
        if jug1 == goal or jug2 == goal:
            return path
        
        next_states = [
            (cap1, jug2, "Fill Jug 1"),
            (jug1, cap2, "Fill Jug 2"),
            (0, jug2, "Empty Jug 1"),
            (jug1, 0, "Empty Jug 2"),
            (max(0, jug1 - (cap2-jug2)), min((jug1+jug2), cap2), "Pour Jug 1 to Jug 2"),
            (min((jug1+jug2), cap1), max(0, jug2 - (cap1-jug1)), "Pour Jug 2 to Jug 1")
        ]
        
        for next_jug1, next_jug2, action in next_states:
            if (next_jug1, next_jug2) not in visited:
                visited.add((next_jug1, next_jug2))
                queue.append((next_jug1, next_jug2, path + [action]))
                
    return None

def main():
    cap1 = 3
    cap2 = 4
    goal = 2
    solution = bfs_solve_water_jug(cap1,cap2, goal)
    if solution:
        print("Solution found!")
        for step in solution:
            print(step)
    else:
        print("No solution found")
        
if __name__ == "__main__":
    main()
                   
        


