from node import Node




def evaluate(n: Node) -> Node:
    if(n == None):
        return Node(None)
    leftVal = evaluate(n.left).value
    rightVal = evaluate(n.right).value
    if(n.value in ['plus', '+']):
        result = Node(leftVal + rightVal)
    elif(n.value in ['minus', '-']):
        result = Node(leftVal - rightVal)
    elif(n.value in ['multiply', '*', 'x']):
        result = Node(leftVal * rightVal)
    elif(n.value in ['divide', '/']):
        result = Node(int(leftVal / rightVal))
    else:
        if(str(n.value).isnumeric() == False):
            raise TypeError("Only integers are allowed")

        else:
            result = Node(int(n.value))
   
    return result
