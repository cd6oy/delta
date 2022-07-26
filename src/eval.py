from node import Node




def evaluate(n: Node) -> Node:
    if(n.value in ['plus', '+']):
        result = int(n.left.value) + int(n.right.value)
    elif(n.value in ['minus', '-']):
        result = int(n.left.value) - int(n.right.value)
    elif(n.value in ['multiply', '*', 'x']):
        result = int(n.left.value) * int(n.right.value)
    elif(n.value in ['divide', '/']):
        result = int(n.left.value) / int(n.right.value)
    return Node(int(result))