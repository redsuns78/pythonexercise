def get_lowest_cost_node(costs: dict, processed):
  """ Return a node which has a lowest cost in Costs """
  lowest_cost = float('inf')
  lowest_cost_node = None

  for key, value in costs.items():
    if lowest_cost >= value[0] and key not in processed:
      lowest_cost = value[0]
      lowest_cost_node = key

  return lowest_cost_node

def get_lowest_cost_edge(costs: dict):
  """ Return a edge which has a lowest cost in Costs """
  lowest_cost = float('inf')
  lowest_cost_edge = None

  for edge, cost in costs.items():
    if lowest_cost >= cost:
      lowest_cost = cost
      lowest_cost_edge = edge

  return lowest_cost_edge

class Partition:
  """Union-find structure for maintaining disjoint sets."""
  # ------------------------- nested Position class -------------------------
  class Position:
    def __init__(self, container, e):
      """Create a new position that is the leader of its own group."""
      self._container = container  # reference to Partition instance
      self._element = e
      self._size = 1
      self._parent = self  # convention for a group leader

    def element(self):
      """Return element stored at this position."""
      return self._element

  # ------------------------- nonpublic utility -------------------------
  def get_parent(self, p):
    return p._parent

  def _validate(self, p):
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')

  # ------------------------- public Partition methods -------------------------
  def make_group(self, e):
    """Makes a new group containing element e, and returns its Position."""
    return self.Position(self, e)

  def find(self, p):
    """Finds the group containging p and return the position of its leader."""
    self._validate(p)
    if p._parent != p:
      p._parent = self.find(p._parent)  # overwrite p._parent after recursion
    return p._parent

  def union(self, p, q):
    """Merges the groups containg elements p and q (if distinct)."""
    a = self.find(p)
    b = self.find(q)
    if a is not b:  # only merge if different groups
      if a._size > b._size:
        b._parent = a
        a._size += b._size
      else:
        a._parent = b
        b._size += a._size

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

def MST_PrimJarnik(graph, start) -> dict:
  """Compute a minimum spanning tree of weighted graph g.
  Return a list of edges that comprise the MST """

  # for costs like {0: (0, None), 1: (144, (0, 1, 144)), 2: (184, (0, 2, 184))
  costs = {node: (float('inf'), None) for node in graph.keys()}
  costs[start] = (0, None)  # For Start Node

  processed = []            # manage processed nodes
  node = get_lowest_cost_node(costs, processed)   # Get Start Node

  while node is not None:
    for dst, cost in graph[node].items():
      if dst not in processed:
        # see if edge (node,dst) better connects dst to the growing tree
        if cost < costs[dst][0]:           # cost : cost of edge(node, dst),
                                           # costs[dst][0]: current costs of dst node
           costs[dst] = (cost, (node, dst, graph[node][dst]))
    processed.append(node)

    node = get_lowest_cost_node(costs, processed)

  return costs

def MST_Kruskal(graph) -> dict:
  """Compute a minimum spanning tree of a graph using Kruskal's algorithm.
  Return a list of edges that comprise the MST. """
  tree = {}                   # to return edges and costs in spanning tree
  costs = {}                  # to manage edges and costs list should be dealt with
  forest = Partition()        # keeps track of forest clusters
  position = {}               # map each node to its Partition entry

  # initialize forests which consist of one vertex
  for vertex, dst in graph.items():
    position[vertex] = forest.make_group(vertex)
    # list every edge with cost as a dictionary
    for dst_vertex, cost in dst.items():
      costs[(vertex, dst_vertex)] = cost

  size = len(position)

  while len(tree) != size - 1 and costs:
  # tree not spanning and unprocessed edges remain
    edge = get_lowest_cost_edge(costs)
    cost = costs[edge]
    del(costs[(edge)])    # delete cost of the edge
    u, v = edge

    a = forest.find(position[u])
    b = forest.find(position[v])

    if a != b:
      tree[edge] = cost
      forest.union(a,b)

  # Test every position has the same parent
  for key, value in position.items():
    print(key, forest.get_parent(value))

  return tree

from collections import defaultdict

def solution(n, costs_table):
  '''
  :param n: Number of vertices
  :param costs_table: Edge and Weight lists like [[0, 1, 12], [0, 2, 112], [1, 2, 21] .... ]
  :return: The cost of a Minimum Spanning Tree
  '''
  # form a directed graph using dictionary
  # like {0:{1:12, 2:112}, 1:{2:21}, .... }
  graph = defaultdict(dict)
  for edge in costs_table:
    graph[edge[0]].update({edge[1]:edge[2]})
    graph[edge[1]].update({edge[0]:edge[2]})
  # Set the start node for Dijkstra's and Prim
  start = 'BWI' if graph.get('BWI', 0) else 0

  # --- Dijkstra's Algorithm ---
  costs = dijkstras(graph, start)
  edges = [value[1] for value in costs.values()]
  totalcost = sum([edge[2] for edge in edges if edge is not None])
  print('Dijkstra', totalcost)

  # --- Prim Jarnik Algrithm ---
  costs = MST_PrimJarnik(graph, start)
  totalcost = sum([cost[0] for cost in costs.values()])
  print('Prim', totalcost)

  # --- Kruskal's Algorithm ---
  tree = MST_Kruskal(graph)
  totalcost = sum([cost for cost in tree.values()])
  print('Kruskal', totalcost)

  return totalcost

if __name__ == '__main__':
    solution(9, [('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
    ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
    ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
    ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
    ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
    ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
    ('JFK', 'BOS', 187)])

    # solution(9, [[7, 8, 337], [7, 4, 2704], [7, 3, 1846], [7, 6, 1464], [8, 6, 1235], [8, 5, 2342], [6, 3, 802],
    #              [6, 0, 1391], [6, 5, 1121], [3, 4, 867], [3, 1, 849], [3, 0, 740], [3, 2, 621], [5, 2, 946],
    #              [5, 0, 1090], [5, 4, 1258], [2, 0, 184], [0, 1, 144], [0, 4, 187]])