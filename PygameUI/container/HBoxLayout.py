import time
from . import Container
from .. import widget


class HBoxLayout(Container.Container):
    def __init__(self, x, y, margin:int=0, width=0, height=0, clip_mode:bool=False):
        super().__init__(x, y, width, height, clip_mode)
        self.margin = margin
    def GetAllWidth(self):
        width = 0
        for w in self.widget_list:
            if w.visible:
                width += w.width
                width += self.margin
        if width >= self.margin:
            width -= self.margin
        return width
    def GetAllHeight(self):
        height = []
        for w in self.widget_list:
            if w.visible:
                height.append(w.height)
        return max(height, default=0)
    def Layout(self, w:widget.Widget.Widget):
        if not self.visible:
            return False
        PosX = self.x
        for w in self.widget_list:
            if not w.visible:
                continue
            w.parent = None
            if isinstance(w, Container.Container):
                w.Move(PosX, self.y, False)
                if w.call_event == w.call_event.ShallowUpdate:
                    w.Layout(w)
            else:
                w.Move(PosX, self.y)
            w.parent = self
            PosX += w.width + self.margin
        super().Layout(self)
        return True