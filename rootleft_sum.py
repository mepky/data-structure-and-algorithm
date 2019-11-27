def left_tree_sum(A,B):
    if not A:
        return 0
    root=A
    target=B
    target_sum-=root.val
    if not root.left or root.right or target_sum==0:
        return 1
    return left_tree_sum(root.left,target) or left_tree_sum(root.right,target)
