
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

def CheckAreaInArea(check_area:Area, sub_area:Area):
    if check_area.x <= sub_area.x and check_area.x+check_area.width >= sub_area.x+sub_area.width and check_area.y <= sub_area.y and check_area.y+check_area.height >= sub_area.y+sub_area.height:
        return True
    return False
