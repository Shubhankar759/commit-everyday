'''
Problem Statment 
https://acm.timus.ru/problem.aspx?space=1&num=1569
'''

def BFS(graph,number_of_nodes,start_node):
    seeker=[start_node]
    flags = [True]*(number_of_nodes+1)
    flags[start_node] = False
    record = []
    while len(seeker):
        node = seeker.pop(0)
        for i in graph:
            if i[0]==node and flags[i[1]]:
                seeker.append(i[1])
                flags[i[1]] = False
                record.append(i)
            elif i[1]==node and flags[i[0]]:
                seeker.append(i[0])
                flags[i[0]] = False
                record.append(i)
    return record

def farthest_node(graph, number_of_nodes, start_node):
    seeker = [start_node]
    flags = [True] * (number_of_nodes + 1)
    flags[start_node] = False
    distance = [0] * (number_of_nodes + 1) 
    
    while len(seeker):
        node = seeker.pop(0)
        for i in graph:
            if i[0] == node and flags[i[1]]:
                seeker.append(i[1])
                flags[i[1]] = False
                distance[i[1]] = distance[node] + 1  
            elif i[1] == node and flags[i[0]]:
                seeker.append(i[0])
                flags[i[0]] = False
                distance[i[0]] = distance[node] + 1  
    
    farthest = distance.index(max(distance)) 
    return farthest, max(distance)

def compute_diameter(record, number_of_nodes):
   
    u, _ = farthest_node(record, number_of_nodes, 1)  
    _, diameter = farthest_node(record, number_of_nodes, u) 
    return diameter

number_of_nodes  = int(input("Enter Number of Nodes:"))
number_of_edges  = int(input("Enter Number of Edges:"))
graph = []
for i in range(0,number_of_edges):
    temp =  list(map(int, input(f"Enter Edges {i+1}:").split(',')))
    graph.append(temp)

best_diameter = 10000
best_tree = []

for root in range(1,number_of_nodes+1):
    record = BFS(graph,number_of_nodes,root)
    diameter = compute_diameter(record, number_of_nodes)
    if diameter < best_diameter:
        best_diameter = diameter
        best_tree = record

print(best_tree) 