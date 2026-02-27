from abc import abstractmethod
from enum import Enum

import pygame
from .. import widget
from typing import Self

class WidgetEvent(Enum):
    MouseIn='MouseIn'
    MouseExit='MouseExit'
    Hover='Hover'
    Update='Update'
    ShallowUpdate='ShallowUpdate'
    AddWidget='AddWidget'
    RemoveWidget='RemoveWidget'

class MarginError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
class Container(widget.Widget.Widget):
    Events = WidgetEvent
    def __init__(self, x:int, y:int, width:int=0, height:int=0, clip_mode:bool=False):
        self.clip_mode = clip_mode
        if self.clip_mode:
            super().__init__(x, y, width, height)
        else:
            super().__init__(x, y, 0, 0)
        self._width = width
        self._height = height
        self.widget_list:list[widget.Widget.Widget] = []
        self.When(self.cevent.AddWidget, self.Layout)
        self.When(self.cevent.RemoveWidget, self.Layout)
        self.When(self.cevent.Update, self.Layout)
    def GetAllWidth(self):
        width = 0
        for w in self.widget_list:
            if w.visible:
                width += w.width
        return width
    def GetAllHeight(self):
        height = 0
        for w in self.widget_list:
            if w.visible:
                height += w.height
        return height
    @property
    def width(self):
        if self.clip_mode:
            return self._width
        return self.GetAllWidth()
    @width.setter
    def width(self, val):
        if self.clip_mode:
            self._width = val
        else:
            return
    @property
    def height(self):
        if self.clip_mode:
            return self._height
        return self.GetAllHeight()
    @height.setter
    def height(self, val):
        if self.clip_mode:
            self._height = val
        else:
            return
    def RemoveWidget(self, w:widget.Widget.Widget):
        w.Register()
        self.widget_list.remove(w)
        self.Emit(self.cevent.RemoveWidget)
        w.UnWhen(w.cevent.Update, self.Layout)
        if isinstance(w, Container):
            w.UnWhen(w.cevent.ShallowUpdate,  self.Layout)
    def AddWidget(self, w:widget.Widget.Widget|Self):
        w.DoesNotParticipateInStandardControlFlow()
        self.widget_list.append(w)
        w.parent = self
        w.When(w.cevent.Update, self.Layout)
        if isinstance(w, Container):
            w.When(w.cevent.ShallowUpdate, self.Layout)
        self.Emit(self.cevent.AddWidget)
    def Layout(self, w:widget.Widget.Widget, shallow_update=False):
        if isinstance(self.parent, Container):
            self.Emit(self.cevent.ShallowUpdate)
    def HandleEvent(self, event):
        if not super().HandleEvent(event):
            return False
        for w in self.widget_list:
            w.HandleEvent(event)
        return True
    def Draw(self, surface:pygame.Surface):
        if not super().Draw(surface):
            return False
        if self.clip_mode:
            OldArea = surface.get_clip()
            Area = pygame.rect.Rect(self.x, self.y, self.width, self.height)

            surface.set_clip(Area)
        # pygame.draw.rect(surface, self.theme.Data.SubColor, Area)
        for w in self.widget_list:
            w.Draw(surface)
        if self.clip_mode:
            surface.set_clip(OldArea)
        return True
    def Update(self):
        if not super().Update():
            return False
        for w in self.widget_list:
            w.Update()
        return True
    def Move(self, x, y, update=True):
        if not super().Move(x, y):
            return False
        self.x = x
        self.y = y
        if update:
            self.Emit(self.cevent.Update)
        return True