def print_tree(root):
    if root == None:
        return ;
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)