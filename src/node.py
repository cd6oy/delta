from typing import List


class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None
    def toString(self):
        if self.left == None and self.right == None:
            r = str(self.value)
        else:
            r = '('
            r = r+ str(self.value)
            r = r+ ' '
            if self.left != None:  
                r = r+str(self.left.toString())
            else:
                r = r+ str('')
            r = r+' '
            if self.right != None:
                r = r+str(self.right.toString())
            else:
                r = r+str('')
            r = r+')'
        return r
class Unit:
    def __init__(self, value: str):
        self.value = value
        self.args = list[Unit]()
    def toString(self):
        if len(self.args) == 0:
            r = str(self.value)
        else:
            r = '('
            r = r+ str(self.value)
            r = r+ ' '
            if self.args[0] != None:  
                r = r+str(self.args[0].toString())
            else:
                r = r+ str('')
            r = r+' '
            if self.args[1] != None:
                r = r+str(self.args[1].toString())
            else:
                r = r+str('')
            r = r+')'
        return r
