import heapq

def dijkstra(graph, start):
    # Store shortest distances
    distances = {}

    # Initialize all distances as infinity
    for node in graph:
        distances[node] = float('inf')

    # Distance to start node = 0
    distances[start] = 0

    # Priority queue
    pq = []
    heapq.heappush(pq, (0, start))

    # To store shortest path
    previous = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Visit neighbors
        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            # Relaxation step
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


# Graph representation
graph = {
    'A': [('B', 4), ('C', 1), ('D', 7)],
    'B': [('A', 4), ('D', 2)],
    'C': [('A', 1), ('D', 5)],
    'D': [('A', 7), ('B', 2), ('C', 5)]
}

# Run algorithm
distances, previous = dijkstra(graph, 'A')

# Print shortest distances
print("Shortest Distances:")
for node in distances:
    print(f"A -> {node} = {distances[node]}")

# Print previous nodes
print("\nPrevious Nodes:")
print(previous)