from node import Unit




def evaluate(n: Unit) -> Unit:
    if(n == None):
        return Unit(None)
    left = evaluate(n.args[0])
    right = evaluate(n.args[1])
    print("LEFT: " + left.toString())
    print('RIGHT: ' + right.toString())
    print('nVal: ' + n.toString())
    leftVal = left.value
    rightVal = right.value
    if(n.value in ['plus', '+']):
        result = Unit(leftVal + rightVal)
    elif(n.value in ['minus', '-']):
        result = Unit(leftVal - rightVal)
        print('RESULT: ' + result.toString())
    elif(n.value in ['multiply', '*', 'x']):
        result = Unit(leftVal * rightVal)
    elif(n.value in ['divide', '/']):
        result = Unit(int(leftVal / rightVal))
    else:
        if(str(n.value).isnumeric() == False):
            raise TypeError("Only integers are allowed")

        else:
            result = Unit(int(n.value))
    #print(result.value)
    return result
