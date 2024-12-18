def read_heuristics(file_path):
    heuristics = {}
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            if len(data) >= 2:  
                heuristics[data[0]] = int(data[1])
    return heuristics

def read_graph(file_path):
    graph = {}
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            if len(data) < 3:  
                continue
            neighbors = {}
            for idx in range(2, len(data), 2): 
                neighbors[data[idx]] = int(data[idx + 1])
            graph[data[0]] = neighbors
    return graph

# A* Search Algorithm
import heapq

def astar_search(start_node, destination, graph, heuristics):
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))
    
    came_from = {start_node: None}
    cost_so_far = {start_node: 0}
    
    while priority_queue:
        
        current_node = heapq.heappop(priority_queue)[1]
                
        if current_node == destination:
            break
                
        for neighbor, cost in graph.get(current_node, {}).items():
            new_cost = cost_so_far[current_node] + cost  # g(n)
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics.get(neighbor, float('inf'))  # f(n)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_node
    
    return came_from, cost_so_far


def display_path(came_from, cost_so_far, start_node, destination):
   
    if destination not in came_from:
        print("NO PATH FOUND!")
        return
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
    path.reverse()
    print("Path: ", " --> ".join(path))
    print("Total distance: ", cost_so_far[destination], "km")


if __name__ == "__main__":
    file_path = r"E:\CSE422\Lab01.txt"
    
    heuristics = read_heuristics(file_path)
    graph = read_graph(file_path)
    
    start_node = input("Enter the start node: ").strip()
    destination = input("Enter the destination node: ").strip()
    
    if start_node not in heuristics or destination not in heuristics:
        print("Start or destination does not exist.")
    else:
       
        came_from, cost_so_far = astar_search(start_node, destination, graph, heuristics)
        
        display_path(came_from, cost_so_far, start_node, destination)
