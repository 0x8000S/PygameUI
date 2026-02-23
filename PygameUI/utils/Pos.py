from typing import Union

class Position: 
    def __init__(self, x, y):
        self.x= x
        self.y = y
class Area():
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def CheckPosInArea(area:Area, pos:Position) -> bool:
    if pos.x >= area.x and (area.x+area.width) >= pos.x and pos.y >= area.y and (area.y+area.height) >= pos.y:
        return True
    return False