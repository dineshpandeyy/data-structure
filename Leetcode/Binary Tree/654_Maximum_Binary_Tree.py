class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):

    def build(sub_nums):
        if not sub_nums:
            return 
        
        maxValue = max(sub_nums)
        indexMaxValue = sub_nums.index(maxValue)

        root = TreeNode(maxValue)
    
        root.left = build(sub_nums[:indexMaxValue])
        root.right = build(sub_nums[indexMaxValue+1:])

        return root

    return build(nums)