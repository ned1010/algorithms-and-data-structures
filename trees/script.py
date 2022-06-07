from tree import TreeNode 
from breath_first_search import bfs
from bfs import breathfirtsearch
from depth_first_search import dfs


root_node = TreeNode("Desktop")
work_folder = TreeNode("Work")
school_folder = TreeNode("School")
project_folder = TreeNode("Project")

root_node.children = [work_folder, school_folder, project_folder]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
my_horse = TreeNode("Horse.jpg")
my_work = TreeNode("Work.jpg")

work_folder.children = [my_todo, my_work]
school_folder.children = [my_cat, my_horse]
project_folder.children = [my_dog, my_wish]

finding_path = bfs(root_node, "Work.jpg")
finding_path_dfs = bfs(root_node, "Work.jpg")

if finding_path is None:
    print("Path not found")
else:
    print("Path found using BFS")
    for path in finding_path:
        print(path.value)

if finding_path is not None:
    print("Path found using DFS")
    for path in finding_path_dfs:
        print(path.value)
else:
    print("No path found")