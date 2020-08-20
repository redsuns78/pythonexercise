# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# from ..ch09 import HeapPriorityQueue,AdaptableHeapPriorityQueue
# from .partition import Partition

def graph_from_edgelist(E, directed=False):
  """Make a graph instance based on a sequence of edge tuples.

  Edges can be either of from (origin,destination) or
  (origin,destination,element). Vertex set is presume to be those
  incident to at least one edge.

  vertex labels are assumed to be hashable.
  """
  g = Graph(directed)
  V = set()
  for e in E:
    V.add(e[0])
    V.add(e[1])

  verts = {}  # map from vertex label to Vertex instance
  for v in V:
    verts[v] = g.insert_vertex(v)

  for e in E:
    src = e[0]
    dest = e[1]
    element = e[2] if len(e) > 2 else None
    g.insert_edge(verts[src],verts[dest],element)

  return g

def MST_PrimJarnik(graph, start):
  """Compute a minimum spanning tree of weighted graph g.

  Return a list of edges that comprise the MST (in arbitrary order).
  """
  d = {}                               # d[v] is bound on distance to tree
  tree = []                            # list of edges in spanning tree
  costs = {}   # d[v] maps to value (v, e=(u,v))
  processed = []                       # map from vertex to its pq locator

  # for each vertex v of the graph, add an entry to the priority queue, with
  # the source having distance 0 and all others having infinite distance
  for v in graph.keys():
    if len(d) == 0:                                 # this is the first node
      d[v] = 0                                      # make it the root
    else:
      d[v] = float('inf')                           # positive infinity
    costs[v] = (d[v], None)

  node = lowest_pq(costs, processed)
  while node is not None:
    # for key, value in pq.items():
    #   print('pq', key, value)
    # print('------')
    # print('key', key)
    edge = costs[node][1]  # unpack tuple from pq
    processed.append(node)
    # del pq[key]

    # print(u, edge)
    # del pqlocator[u]                                # u is no longer in pq
    if edge is not None:
      tree.append(edge)                             # add edge to tree

    #for link in g.incident_edges(u):
    for v in graph[node]:
      if v not in processed:
      #if v in pq:                            # thus v not yet in tree
        # see if edge (u,v) better connects v to the growing tree
        wgt = graph[node][v]
        if wgt < d[v]:                              # better edge to v?
           d[v] = wgt                                # update the distance
           costs[v] = (d[v], (node, v, wgt))

    node = lowest_pq(costs, processed)
  for node, value in costs.items():
    print('pq', node, value)

  #print(tree)
  return tree
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
def lowest_pq(pq: dict, processed):
  lowest_cost = float('inf')
  lowest_node = None

  for key, value in pq.items():
    if lowest_cost >= value[0] and key not in processed:
      lowest_cost = value[0]
      lowest_node = key

  return lowest_node

from collections import defaultdict
from functools import reduce

if __name__ == '__main__':
  E = (
    ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
    ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
    ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
    ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
    ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
    ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
    ('JFK', 'BOS', 187),
  )

  graph = {node[0] : {} for node in E}
  graph.update({node[1] : {} for node in E})

  for edge in E:
    graph[edge[0]].update({edge[1]:edge[2]})
    graph[edge[1]].update({edge[0]: edge[2]})
  print(graph)

  tree = MST_PrimJarnik(graph, 'PVD')

  result = list(map(lambda x : x[2], tree))
  print(sum(result))


