from tokenizer import tokenizer
from node import Node

def parseTree(input: str, startPos) -> Node and int:
    i = startPos
    n = None
    while i < len(input):
        end = tokenizer(input, i)
        word = input[i: end]
        if(word == '('):
            if(n == None):
                n = Node(None)
            else:
                nextNode = parseTree(str, i)
        elif(word == ')'):
            return n, i
        elif(word == ' '):
            None
    
        else:
            if(n == None):
                n = Node(word)
            elif(n.value == None):
                n.value = word
            elif(n.left == None):
                n.left = Node(word)
            elif(n.right == None):
                n.right = Node(word)
        i = end
    return n, i

def parser(testcase: str):
    return parseTree(testcase, 0)[0]