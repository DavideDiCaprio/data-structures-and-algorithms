def build_directed_graph(edges):
    """
    Build a directed graph from a list of edges.
    
    Args:
        edges: List of tuples (x, y) representing edges from x to y
        
    Returns:
        Dictionary representing the adjacency list of the graph
    """
    graph = {}
    for x, y in edges:
        if x not in graph:
            graph[x] = []
        graph[x].append(y)
        
        if y not in graph:
            graph[y] = []
            
    return graph


def build_undirected_graph(edges):
    """
    Build an undirected graph from a list of edges.
    
    Args:
        edges: List of tuples (x, y) representing edges between x and y
        
    Returns:
        Dictionary representing the adjacency list of the graph
    """
    graph = {}
    for x, y in edges:
        if x not in graph:
            graph[x] = []
        graph[x].append(y)
        
        if y not in graph:
            graph[y] = []
        graph[y].append(x)
            
    return graph
