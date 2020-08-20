from collections import defaultdict
import operator

def get_lowest_cost_node(costs: dict, processed):
  """ Return a node which has a lowest cost in Costs """
  lowest_cost = float('inf')
  lowest_cost_node = None

  for key, value in costs.items():
    if lowest_cost >= value[0] and key not in processed:
      lowest_cost = value[0]
      lowest_cost_node = key

  return lowest_cost_node

def dijkstras(graph, start) -> dict:
  """Compute shortest-path distances from
  start to reachable vertices of graph"""

  # for costs like {0: (0, None), 1: (144, (0, 1, 144)), 2: (184, (0, 2, 184))
  costs = {node: (float('inf'), None) for node in graph.keys()}
  costs[start] = (0, None)    # For Start Node

  processed = []              # manage processed nodes
  node = get_lowest_cost_node(costs, processed)   # Get Start Node

  while node is not None:
    for dst, cost in graph[node].items():
      new_cost = costs[node][0] + cost    # Current Node's cost + Edge's cost for dst Node
      if new_cost < costs[dst][0]:        # Is new_cost lower than dst's cost
        costs[dst] = (new_cost, (node, dst, graph[node][dst]))  # Set new_cost and Edge
    processed.append(node)                # So as not to process again
    node = get_lowest_cost_node(costs, processed)     # Get next Lowest Node

  return costs    # costs like {0: (0, None), 1: (144, (0, 1, 144)), 2: (184, (0, 2, 184))

def solution(N, costs_table, K):
  graph = defaultdict(dict)
  costs_table.sort(key=operator.itemgetter(2), reverse=True)

  for edge in costs_table:
    graph[edge[0]].update({edge[1]:edge[2]})
    graph[edge[1]].update({edge[0]:edge[2]})

  costs = dijkstras(graph, 1)
  return (len([node[0] for node in costs.values() if node[0] <= K]))

if __name__ == '__main__':
    solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
    solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	, 4)