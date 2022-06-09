def tsp(graph, visited, currentPos, n, count, cost):

    # If last node is reached and it has a link to the starting node i.e the source then keep the minimum
    # value out of the total cost of traversal and "ans". Finally return to check for more possible values
    if (count == n and graph[currentPos][0]):
        answer.append(cost + graph[currentPos][0])
        return

    # BACKTRACKING STEP
    # Loop to traverse the adjacency list of currentPos node and increasing the count  by 1 and cost by graph[currentPos][i] value
    for i in range(n):
        if (visited[i] == False and graph[currentPos][i]):
            
            # Mark as visited
            visited[i] = True
            tsp(graph, visited , i, n, count + 1,
                cost + graph[currentPos][i])
            
            # Mark ith node as unvisited
            visited[i] = False


# Driver code
graph, answer = [], []
n = int(input("Enter the Number of Nodes: "))

print(f"\nEnter the {n}x{n} Adjacency Matrix")

for i in range(0,n):
    row = input(f"Enter Row {i} values:").split(" ")
    graph.append([int(value) for value in row])

# list to check if a node has been visited or not
visited = [False for i in range(n)]

# Mark 0th node as visited
visited[0] = True
tsp(graph, visited, 0, n, 1, 0)

# Display minimum weight Hamiltonian Cycle
print("\n The Minimum Path value is: ", min(answer))
