from typing import List



class Unit:
    def __init__(self, value: str):
        self.value = value
        self.args = list[Unit]()
    def toString(self):
        if len(self.args) == 0:
            r = str(self.value)
        else:
            r = '( '
            r = r+ str(self.value)
            r = r+ ' '
            for arg in self.args:
                if arg!= None:  
                    r = r+str(arg.toString())
                else:
                    r = r+ str('')
                r = r+ ' '
            r = r+')'
        return r
    def isNumber(self) -> bool:
        strVal = str(self.value)
        return strVal.isnumeric()
    def isString(self) -> bool:
        strVal = str(self.value)
        return strVal.startswith('"') and strVal.endswith('"')