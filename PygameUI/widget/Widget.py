from abc import abstractmethod
from typing import Any, Callable
from enum import Enum
from ..utils import Pos
from .. import themes
import pygame
pygame.init()

class WidgetManage():
    widgets:list['Widget'] = []
    groups:list['Group'] = []
    @classmethod
    def Register(cls, w:'Widget'):
        if not w in cls.widgets:
            cls.widgets.append(w)
    @classmethod
    def RegisterGroup(cls, g:'Group'):
        if not g in cls.groups:
            cls.groups.append(g)
    @classmethod
    def HandleEvent(cls, events:pygame.event.Event):
        for w in cls.widgets + cls.groups:
            w.HandleEvent(events)
    @classmethod
    def Update(cls):
        for w in cls.widgets + cls.groups:
            w.Update()
    @classmethod
    def Draw(cls, surface: pygame.surface):
        for w in cls.widgets + cls.groups:
            w.Draw(surface)
    @classmethod
    def RemoveWidget(cls, w:'Widget'):
        cls.widgets.remove(w)
    @classmethod
    def RemoveGroup(cls, g:'Group'):
        cls.groups.remove(g)
        g.RemoveAllWidget()

class Group():
    def __init__(self):
        self.widgets:list['Widget'] = []
        self.visible = True
    def Register(self, w:'Widget'):
        if not w in self.widgets:
            w.DoesNotParticipateInStandardControlFlow()
            self.widgets.append(w)
    def HandleEvent(self, events:pygame.event.Event):
        for w in self.widgets:
            w.HandleEvent(events)
    def Update(self):
        for w in self.widgets:
            w.Update()
    def Draw(self, surface: pygame.surface):
        for w in self.widgets:
            w.Draw(surface)
    def RemoveWidget(self, w:'Widget'):
        self.widgets.remove(w)
        WidgetManage.Register(w)
    def RemoveAllWidget(self):
        for w in self.widgets[:]:
            self.RemoveWidget(w)
    def ShowAll(self):
        for w in self.widgets:
            w.Show()
    def HideAll(self):
        for w in self.widgets:
            w.Hide()
    def EnableAll(self):
        for w in self.widgets:
            w.enable = True
    def DisableAll(self):
        for w in self.widgets:
            w.enable = False

class WidgetEvent(Enum):
    MouseIn='MouseIn'
    MouseExit='MouseExit'
    Hover='Hover'
    Update='Update'

class Widget():
    Events = WidgetEvent
    @classmethod
    def GetWidgetEvents(cls) -> Enum:
        return cls.Events
    def __init__(self, x:int, y:int, width:int, height:int, theme:None|themes.Theme.Theme=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parent:Widget = None
        self.theme = themes.GetDefaultTheme()
        if theme is not None:
            self.theme = theme
        self.visible = True
        self.enable = True
        self.cevent:WidgetEvent = self.GetWidgetEvents()
        self._MouseIn:bool = False
        self._MouseExit:bool = False
        self._EventHandlers:dict[WidgetEvent, list[Callable[['Widget']], Any]] = {}
        self.call_event = None
        for i in list(self.GetWidgetEvents()):
            self._EventHandlers[i] = []
        self.Register()
    def Register(self):
        self.parent = None
        WidgetManage.Register(self)
    def DoesNotParticipateInStandardControlFlow(self):
        WidgetManage.RemoveWidget(self)
    def Emit(self, Event:WidgetEvent):
        for e in self._EventHandlers.get(Event):
            self.call_event = Event
            e(self)
    def UnWhen(self, Event:WidgetEvent, Func:Callable[['Widget'], Any]):
        self._EventHandlers[Event].remove(Func)
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
    @abstractmethod
    def Move(self, x:int, y:int) -> bool:
        if self.parent != None:
            return False
        return True
        
    def Hide(self):
        self.visible = False
        self.Emit(self.cevent.Update)
    def Show(self):
        self.visible = True
        self.Emit(self.cevent.Update)

