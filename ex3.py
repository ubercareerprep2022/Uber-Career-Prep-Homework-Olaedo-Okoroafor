def printNumLevels(root, max):
    if root == None:
        return max;

    max += 1
    add_right = printNumLevels(root.right, max)
    add_left = printNumLevels(root.left, max)
    if add_right > add_left:
        max = add_right
    else:
        max = add_left
    return max
    