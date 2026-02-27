import time
from . import Container
from .. import widget


class VBoxLayout(Container.Container):
    def __init__(self, x, y, margin:int=0, width=0, height=0, clip_mode:bool=False):
        super().__init__(x, y, width, height, clip_mode)
        self.margin = margin
    def GetAllWidth(self):
        width = []
        for w in self.widget_list:
            if w.visible:
                width.append(w.width)
        return max(width, default=0)
    def GetAllHeight(self):
        height = 0
        for w in self.widget_list:
            if w.visible:
                height += w.height
                height += self.margin
        if height >= self.margin:
            height -= self.margin
        return height
    def Layout(self, w:widget.Widget.Widget):
        if not self.visible:
            return False
        PosY = self.y
        for w in self.widget_list:
            if not w.visible:
                continue
            w.parent = None
            if isinstance(w, Container.Container):
                w.Move(self.x, PosY, False)
                if w.call_event == w.call_event.ShallowUpdate:
                    w.Layout(w)
            else:
                w.Move(self.x, PosY)
            w.parent = self
            PosY += w.height + self.margin
        super().Layout(self)
        return True