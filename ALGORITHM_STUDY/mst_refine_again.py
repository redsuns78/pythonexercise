def MST_PrimJarnik(graph, start):
  """Compute a minimum spanning tree of weighted graph g.
  Return a list of edges that comprise the MST (in arbitrary order).
  """
  # for each vertex v of the graph, add an entry to the priority queue, with
  # the source having distance 0 and all others having infinite distance
  costs = {node: (float('inf'), None) for node in graph.keys()}
  costs[start] = (0, None)
  processed = []  # manage processed nodes

  node = get_lowest_cost_node(costs, processed)
  while node is not None:
    processed.append(node)
    for dst, cost in graph[node].items():
      if dst not in processed:
        # see if edge (u,v) better connects v to the growing tree
        if cost < costs[dst][0]:           # better edge to v?
           costs[dst] = (cost, (node, dst, graph[node][dst]))
    node = get_lowest_cost_node(costs, processed)

  return costs

def get_lowest_cost_node(costs: dict, processed):
  lowest_cost = float('inf')
  lowest_cost_node = None

  for key, value in costs.items():
    if lowest_cost >= value[0] and key not in processed:
      lowest_cost = value[0]
      lowest_cost_node = key

  return lowest_cost_node

def solution(n, costs):

  graph = {i: {} for i in range(n)}
  for edge in costs:
    graph[edge[0]].update({edge[1]:edge[2]})
    graph[edge[1]].update({edge[0]:edge[2]})

  costs = MST_PrimJarnik(graph, 0)
  print(costs)
  totalcost = sum([cost[0] for cost in costs.values()])
  print(totalcost)

  return totalcost

def MST_Kruskal(g):
  """Compute a minimum spanning tree of a graph using Kruskal's algorithm.
  Return a list of edges that comprise the MST.
  The elements of the graph's edges are assumed to be weights.
  """
  tree = []                   # list of edges in spanning tree
  pq = HeapPriorityQueue()    # entries are edges in G, with weights as key
  forest = Partition()        # keeps track of forest clusters
  position = {}               # map each node to its Partition entry

  for v in g.vertices():
    position[v] = forest.make_group(v)

  for e in g.edges():
    pq.add(e.element(), e)    # edge's element is assumed to be its weight

  size = g.vertex_count()
  while len(tree) != size - 1 and not pq.is_empty():
    # tree not spanning and unprocessed edges remain
    weight,edge = pq.remove_min()
    u,v = edge.endpoints()
    a = forest.find(position[u])
    b = forest.find(position[v])
    if a != b:
      tree.append(edge)
      forest.union(a,b)

  return tree

from collections import defaultdict
from functools import reduce

if __name__ == '__main__':
  solution(9, [[7, 8, 337], [7, 4, 2704], [7, 3, 1846], [7, 6, 1464], [8, 6, 1235], [8, 5, 2342], [6, 3, 802],
               [6, 0, 1391], [6, 5, 1121], [3, 4, 867], [3, 1, 849], [3, 0, 740], [3, 2, 621], [5, 2, 946],
               [5, 0, 1090], [5, 4, 1258], [2, 0, 184], [0, 1, 144], [0, 4, 187]])

  #
  # E = (
  #   ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
  #   ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
  #   ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
  #   ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
  #   ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
  #   ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
  #   ('JFK', 'BOS', 187),
  # )
  #
  # graph = {node[0] : {} for node in E}
  # graph.update({node[1] : {} for node in E})
  #
  # for edge in E:
  #   graph[edge[0]].update({edge[1]:edge[2]})
  #   graph[edge[1]].update({edge[0]: edge[2]})
  # print(graph)
  #
  # costs = MST_PrimJarnik(graph, 'PVD')
  # print(costs)
  # #
  # # result = list(map(lambda x : x[2], tree))
  # # print(sum(result))