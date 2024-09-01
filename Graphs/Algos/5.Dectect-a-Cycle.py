from collections import deque

def bfsCycleDetection(graph, start_node):
    visited = set()
    queue = deque([(start_node, -1)])  # (node, parent)
    
    while queue:
        node, parent = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, node))
            elif neighbor != parent:  # cycle detected
                return True
    
    return False

def is_cycle(graph):
    visited = set()
    
    for node in graph:# for multiple connected components
        if node not in visited:
            if bfsCycleDetection(graph, node):
                return True
            
    return False

# time complexity: O(V + E)
# space complexity: O(V + E)



def dfsCycleDetection(graph, start_node):
    visited = set()
    stack = [(start_node, -1)]  # (node, parent)
    
    while stack:
        node, parent = stack.pop()
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, node))
                elif neighbor != parent:  # Cycle detected
                    return True
    
    return False

def is_cycle(graph):
    visited = set()
    
    for node in graph:
        if node not in visited:
            if dfsCycleDetection(graph, node):
                return True
            
    return False

# time complexity: O(V + E) 
# space complexity: O(V + E) 
