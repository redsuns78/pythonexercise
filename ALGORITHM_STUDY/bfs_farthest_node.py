from collections import deque

def bfs(graph, start):
  queue = deque()
  queue.append([start, 1])
  visited = {}
  max_level = 0

  while(queue):
    node, level = queue.popleft()
    if node not in visited:
      visited[node] = level
      if max_level < level:
        max_level = level

      if node in graph:
        for subnode in graph[node]:
          queue.append([subnode, level+1])

  return visited, max_level

from collections import defaultdict

def solution(n, edges):
  graph = defaultdict(dict)
  for edge in edges:
    graph[edge[0]].update({edge[1]:1})
    graph[edge[1]].update({edge[0]:1})

  visited, max_level = bfs(graph, 1)
  return len([node for node in visited.values() if node == max_level])

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))