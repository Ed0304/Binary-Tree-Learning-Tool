# Traversals
# 1. Preorder: Root-> Left -> Right
# 2. Inorder: Left -> Root -> Right
# 3. Inorder: Left -> Right -> Root

def preorder(node,result=None):
    if result is None:
        result = []
    
    if node is None:
        return result

    result.append(node.value)
    preorder(node.left,result)
    preorder(node.right,result)

    return result

def inorder(node,result=None):
    if result is None:
        result = []
    
    if node is None:
        return result
    
    inorder(node.left,result)
    result.append(node.value)
    inorder(node.right)

    return result

def postorder(node,result=None):
    if result is None:
        result = []

    if node is None:
        return result
    
    postorder(node.left,result)
    postorder(node.right,result)
    result.append(node.value)

    return result

# "Step functions" to accomodatee the user when learning.
def inorder_step(node):
    if node is None:
        return

    yield ("move", f"Go LEFT from node {node.value}")
    yield from inorder_step(node.left)

    yield ("visit", f"VISIT node {node.value} → write it down")
    yield node.value

    yield ("move", f"Go RIGHT from node {node.value}")
    yield from inorder_step(node.right)

    yield ("return", f"RETURN to parent of {node.value}")

def preorder_step(node):
    if node is None:
        return

    yield ("visit", f"VISIT node {node.value} → write it down")
    yield node.value

    yield ("move", f"Go LEFT from node {node.value}")
    yield from preorder_step(node.left)

    yield ("move", f"Go RIGHT from node {node.value}")
    yield from preorder_step(node.right)

    yield ("return", f"RETURN to parent of {node.value}")

def postorder_step(node):
    if node is None:
        return

    yield ("move", f"Go LEFT from node {node.value}")
    yield from postorder_step(node.left)

    yield ("move", f"Go RIGHT from node {node.value}")
    yield from postorder_step(node.right)

    yield ("visit", f"VISIT node {node.value} → write it down")
    yield node.value

    yield ("return", f"RETURN to parent of {node.value}")
