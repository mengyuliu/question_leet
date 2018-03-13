class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == '#' else TreeNode(int(val))
             for val in string.strip('{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


# deserialize()
Input =	deserialize('{3,9,20,#,#,15,7}')
print (Input.right.right.val)