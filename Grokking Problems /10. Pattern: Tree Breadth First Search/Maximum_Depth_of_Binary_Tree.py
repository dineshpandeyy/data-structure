class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_max_depth(root):
    if not root:
        return 0
        
    left = find_max_depth(root.left)
    right = find_max_depth(root.right)

    return 1 + max(left, right)
    
def main():
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  print("Tree Maximum Depth: " + str(find_max_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Maximum Depth: " + str(find_max_depth(root)))


main()