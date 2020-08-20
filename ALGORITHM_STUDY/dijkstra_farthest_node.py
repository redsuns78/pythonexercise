def get_lowest_node(costs, processed):
  lowest_cost = float('inf')
  lowest_node = None

  for node, cost in costs.items():
    if cost < lowest_cost and (node not in processed):
      lowest_cost = cost
      lowest_node = node

  return lowest_node

def dijkstra(graph: dict, start, n):
  costs = {node: float('inf') for node in range(1, n+1)}
  costs[1] = 0

  #print(costs)
  processed = []
  node = get_lowest_node(costs, processed)
  max_cost = 0

  while node is not None:
    processed.append(node)
    for dst, cost in graph[node].items():
      new_cost = costs[node] + cost
      if new_cost < costs[dst]:
        costs[dst] = new_cost

        if new_cost > max_cost:
          max_cost = new_cost

    node = get_lowest_node(costs, processed)

  return len([node for node in costs.values() if node == max_cost])

from collections import defaultdict

def solution(n, edges):

  graph = defaultdict(dict)
  for edge in edges:
    graph[edge[0]].update({edge[1]:1})
    graph[edge[1]].update({edge[0]:1})
  print(graph)

  return dijkstra(graph, 1, n)

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))