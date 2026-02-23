from abc import ABC, abstractmethod
from typing import Any, Callable, Optional
from enum import Enum
from ..utils import Pos
from .. import themes
import pygame
pygame.init()

class WidgetManage():
    widgets:list['Widget'] = []
    @classmethod
    def HandleEvent(cls, events:pygame.event.Event):
        for w in cls.widgets:
            w.HandleEvent(events)
    @classmethod
    def Update(cls):
        for w in cls.widgets:
            w.Update()
    @classmethod
    def Draw(cls, surface: pygame.surface):
        for w in cls.widgets:
            w.Draw(surface)

class WidgetEvent(Enum):
    MouseIn='MouseIn',
    MouseExit='MouseExit',
    Hover='Hover'

class Widget():
    Events = WidgetEvent
    @classmethod
    def GetWidgetEvents(cls) -> Enum:
        return cls.Events
    def __init__(self, x:int, y:int, width:int, height:int, parent:Optional['Widget']=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parent = parent
        self.theme = themes.GetDefaultTheme()
        self.visible = True
        self.enable = True
        self.cevent:WidgetEvent = self.GetWidgetEvents()
        self._MouseIn:bool = False
        self._MouseExit:bool = False
        self._EventHandlers:dict[WidgetEvent, list[Callable[['Widget']], Any]] = {}
        for i in list(self.GetWidgetEvents()):
            self._EventHandlers[i] = []
        print(self._EventHandlers)
        WidgetManage.widgets.append(self)
    def Emit(self, Event:WidgetEvent):
        for e in self._EventHandlers.get(Event):
            e(self)
    def When(self, Event:WidgetEvent, Func:Callable[['Widget'], Any]):
        self._EventHandlers[Event].append(Func)
    def HandleEvent(self, event:pygame.event.Event) -> bool:
        if not self.enable or not self.visible:
            return False
        return True
    def Update(self) -> bool:
        if not self.enable or not self.visible:
            return False
        MousePos = pygame.mouse.get_pos()
        if MousePos != (0,0):
            if Pos.CheckPosInArea(Pos.Area(self.x, self.y, self.width, self.height), Pos.Position(MousePos[0], MousePos[1])):
                if not self._MouseIn:
                    self._MouseIn = True
                    self._MouseExit = False
                    self.Emit(self.cevent.MouseIn)
                    self.Emit(self.cevent.Hover)
            else:
                self._MouseIn = False
                self._MouseExit = True
                self.Emit(self.cevent.MouseExit)
        return True
    @abstractmethod
    def Draw(self, surface:pygame.surface) -> bool:
        if not self.visible:
            return False
        return True


    def Hide(self):
        self.visible = False
    def Show(self):
        self.visible = True

