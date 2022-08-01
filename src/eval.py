from node import Node




def evaluate(n: Node) -> Node:
    if(n == None):
        return Node(None)
    left = evaluate(n.left)
    right = evaluate(n.right)
    print("LEFT: " + left.toString())
    print('RIGHT: ' + right.toString())
    print('nVal: ' + n.toString())
    leftVal = left.value
    rightVal = right.value
    if(n.value in ['plus', '+']):
        result = Node(leftVal + rightVal)
    elif(n.value in ['minus', '-']):
        result = Node(leftVal - rightVal)
        print('RESULT: ' + result.toString())
    elif(n.value in ['multiply', '*', 'x']):
        result = Node(leftVal * rightVal)
    elif(n.value in ['divide', '/']):
        result = Node(int(leftVal / rightVal))
    else:
        if(str(n.value).isnumeric() == False):
            raise TypeError("Only integers are allowed")

        else:
            result = Node(int(n.value))
    #print(result.value)
    return result
