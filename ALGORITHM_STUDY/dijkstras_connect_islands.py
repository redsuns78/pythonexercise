def lowest_node(costs: dict, processed):
  lowest_cost = float('inf')
  lowest_node = None

  for key, cost in costs.items():
    if lowest_cost > cost and key not in processed:
      lowest_cost = cost
      lowest_node = key

  return lowest_node

def dijkstras(graph, start, n):
  '''
  :return: costs
  '''
  costs = {i: float('inf') for i in range(n)}
  costs[start] = 0
  parents = {i: None for i in range(n)}
  processed = []

  # print(costs)

  node = lowest_node(costs, processed)

  while node is not None:
  #while(len(processed) <= n):
    if node in graph:
      for dst, cost in graph[node].items():
    #    print(node, dst)
        if costs[node] + cost < costs[dst]:
          costs[dst] = costs[node] + cost
          parents[dst] = node
    processed.append(node)
    node = lowest_node(costs, processed)

  print('parents', parents)
  print('costs', costs)

  return parents



def solution(n, costs):

  if n == 1:
    return 1

  graph = {i: {} for i in range(n)}

  for edge in costs:
    graph[edge[0]].update({edge[1]:edge[2]})
    graph[edge[1]].update({edge[0]:edge[2]})

  print(graph)
  minimun = float('inf')

  for i in range(n):
    result = 0

    parents = dijkstras(graph, i, n)
    for key, parent in parents.items():
      if parent in graph[key]:
        result += graph[key][parent]

    if minimun > result and result != 0:
      minimun = result

    print('result', i, ' ', result)

    # print('costs_table', costs_table)
    # print('graph', graph)
    # print('parents', parents)

  print(minimun)
  return minimun

if __name__ == '__main__':
    # solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
    # solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])
    # solution(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 3]])
    # solution(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 3]])
    # solution(4, [[0, 1, 1], [0, 2, 4], [0, 3, 5], [1, 2, 2], [1, 3, 6], [2, 3, 3]])
    # solution(5, [[0, 1, 1], [1, 2, 2], [2, 3, 1], [3, 4, 2], [0, 4, 100]])
    # solution(5, [[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]])
    # solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]])
    # solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])
    # solution(4, [[0, 1, 1], [0, 2, 2], [2, 3, 1]])
    #solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
    solution(9, [[7, 8, 337], [7, 4, 2704], [7, 3, 1846],[7, 6, 1464], [8, 6, 1235], [8, 5, 2342],[6, 3, 802], [6, 0, 1391], [6, 5, 1121],[3, 4, 867], [3, 1, 849], [3, 0, 740],  [3, 2, 621], [5, 2, 946], [5, 0, 1090],[5, 4, 1258], [2, 0, 184], [0, 1, 144],[0, 4, 187]])

    print(144+187+184+946+621+802+1235+337)