from tokenizer import tokenizer
from tree import Tree
from tree import Node

def parse(input: str) -> Tree:
    i = 0
    n = None
    while i < len(input):
        end = tokenizer(input, i)
        word = input[i: end]
        if(word == '('):
            n = Node(None)
        elif(word == ')'):
            return Tree(n)
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
    return n
