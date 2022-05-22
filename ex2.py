def printLevelByLevel(li):
    kids = []
    if len(li) == 0:
         return ;

    for node in li:
        print(node.data)
        if node.left != None:
            kids.append(node.left)
        if node.right != None:
            kids.append(node.right)
            
    printLevelByLevel(kids)