class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution
    
def bfs(graph, initialState, goalState):
    frontier = [initialState]
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in explored and child not in frontier:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

graph1 = {
        "A": Node("A", None, ["B", "C","E"], None),
        "B": Node("B", None, ["A","D", "E"], None),
        "C": Node("C", None, ["A","F","G"], None),
        "D": Node("D", None, ["B","E"], None),
        "E": Node("E", None, ["A","B","D"], None),
        "F": Node("F", None, ["C"], None),
        "G": Node("G", None, ["C"], None)
    }
graph2 = {
    "Arad": Node("Arad", None, ["Zerind", "Timisoara","Sibiu"], None),
    "Zerind": Node("Zerind", None, ["Arad","Oradea"], None),
    "Timisoara": Node("Timisoara", None, ["Arad","Lugoj"], None),
    "Sibiu": Node("Sibiu", None, ["Arad","Oradea","Fagaras","Rimnicu Vilcea"], None),
    "Oradea": Node("Oradea", None, ["Zerind","Sibiu"], None),
    "Lugoj": Node("Lugoj", None, ["Timisoara","Mehadia"], None),
    "Fagaras": Node("Fagaras", None, ["Sibiu","Bucharest"], None),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, ["Sibiu","Pitesti","Craiova"], None),
    "Mehadia": Node("Mehadia", None, ["Lugoj","Dobreta"], None),
    "Bucharest": Node("Bucharest", None, ["Fagaras","Pitesti","Giurgiu","Urziceni"], None),
    "Pitesti": Node("Pitesti", None, ["Rimnicu Vilcea","Bucharest","Craiova"], None),
    "Craiova": Node("Craiova", None, ["Rimnicu Vilcea","Pitesti","Dobreta"], None),
    "Dobreta": Node("Dobreta", None, ["Mehadia","Craiova"], None),
    "Giurgiu": Node("Giurgiu", None, ["Bucharest"], None),
    "Urziceni": Node("Urziceni", None, ["Bucharest","Hirsova","Vaslui"], None),
    "Hirsova": Node("Hirsova", None, ["Urziceni","Eforie"], None),
    "Vaslui": Node("Vaslui", None, ["Urziceni","Iasi"], None),
    "Eforie": Node("Eforie", None, ["Hirsova"], None),
    "Iasi": Node("Iasi", None, ["Vaslui","Neamt"], None),
    "Neamt": Node("Neamt", None, ["Iasi"], None)
}

puzzle = [
    ['#', '#', '#', '#', '#', 'E', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '#', 'S', '#', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

def find_start(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if(puzzle[i][j] == 'S'):
                return (i,j)
    return None

print(find_start(puzzle)[0])
def find_end(puzzle):
    for i in len(puzzle):
        for j in len(puzzle[0]):
            if(puzzle[i][j] == 'E'):
                return (i,j)
    return None
def initilze_queue(puzzle):
    matrix = []
    for i in range(len(puzzle)):
        row = []
        for j in range(len(puzzle[0])):
            row.append(False)
        matrix.append(row)
        
    return matrix
def solve_puzzle(puzzle):
    R,C = len(puzzle), len(puzzle[0])
    start = find_start(puzzle)
    
    queue = []
    explored = initilze_queue(puzzle)
    queue.append((start[0],start[1], 0))
    # you can go up, down,left,and right
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    while(queue):
        current_node = queue.pop(0)
        current_x = current_node[0]
        current_y = current_node[1]
        current_cost = current_node[2]
        explored[current_node[0]][current_node[1]] = True
        if(puzzle[current_x][current_y] == "E"):
            return current_cost
        for neighbour in directions:
            new_x = current_x + neighbour[0]
            new_y = current_y + neighbour[1]
            #check if the new coordinates are withing the boundary
            if(new_x <0 or new_x >= R or new_y<0 or new_y>= C or puzzle[new_x][new_y] == '#' or explored[new_x][new_y] == True ):
                continue
            else:
                queue.append((new_x,new_y, current_cost + 1))
                
        
print(solve_puzzle(puzzle))