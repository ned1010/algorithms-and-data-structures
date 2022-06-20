from bfs_graph import bfs
from dfs_graph import dfs

some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))