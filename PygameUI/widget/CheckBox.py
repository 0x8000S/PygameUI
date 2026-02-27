import pygame
from . import Widget
from enum import Enum
from .. import widget

class WidgetEvent(Enum):
    MouseIn='MouseIn'
    MouseExit='MouseExit'
    Hover='Hover'
    Update='Update'
    Click='Click'
    Change='Change'

class CheckBox(Widget.Widget):
    Events = WidgetEvent
    def __init__(self, text:str, x, y, theme=None):
        super().__init__(x, y, 0, 0, theme)
        self.theme_border = self.theme.Data.BorderColor
        self.text = widget.Label.Label(text, self.theme.Font.FontSize, self.x, self.y)
        self.text.When(self.text.cevent.Update, self.Reset)
        self.text.DoesNotParticipateInStandardControlFlow()
        self.outline = pygame.rect.Rect(self.x, self.y, self.text.height, self.text.height)
        self.point = pygame.rect.Rect(0, 0, self.outline.width-8, self.outline.width-8)
        self.point.topleft = (self.outline.x+self.outline.width/2-self.point.width/2, self.outline.y+self.outline.height/2-self.point.height/2)
        self.text.Move(self.outline.x+self.outline.width+10, self.outline.y)
        self.width = self.outline.width + 10 + self.text.width
        self.height = self.text.height
        self.clicked = False
        self.When(self.cevent.MouseIn, self._MouseInEvent)
        self.When(self.cevent.MouseExit, self._MouseExitEvent)
    def _MouseInEvent(self, w:Widget.Widget):
        self.theme_border = self.theme.Data.BorderHoverColor
    def _MouseExitEvent(self, w:Widget.Widget):
        self.theme_border = self.theme.Data.BorderColor
    def HandleEvent(self, event) -> bool:
        if not super().HandleEvent(event):
            return False
        if self._MouseIn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.Emit(self.cevent.Click)
                    self.clicked = not self.clicked
                    self.Emit(self.cevent.Change)
        self.text.HandleEvent(event)
        return True
    def Update(self) -> bool:
        if not super().Update():
            return False
        self.text.Update()
        return True
    def Draw(self, surface:pygame.surface.Surface) -> bool:
        if not super().Draw(surface):
            return False
        pygame.draw.rect(surface, self.theme_border, self.outline, 2)
        self.text.Draw(surface)
        if self.clicked:
            pygame.draw.rect(surface, self.theme.Data.MainColor, self.point)
        return True
    def Reset(self, w:Widget.Widget, update=True):
        self.outline.topleft = (self.x, self.y)
        self.text.Move(self.outline.x+self.outline.width+10, self.outline.y)
        self.point.topleft = (self.outline.x+self.outline.width/2-self.point.width/2, self.outline.y+self.outline.height/2-self.point.height/2)
        self.outline = pygame.rect.Rect(self.x, self.y, self.text.height, self.text.height)
        self.point = pygame.rect.Rect(0, 0, self.outline.width-8, self.outline.width-8)
        self.point.topleft = (self.outline.x+self.outline.width/2-self.point.width/2, self.outline.y+self.outline.height/2-self.point.height/2)
        self.text.Move(self.outline.x+self.outline.width+10, self.outline.y)
        self.width = self.outline.width + 10 + self.text.width
        self.height = self.text.height
        if update:
            self.Emit(self.cevent.Update)
    def Move(self, x, y):
        if not super().Move(x,y):
            return False
        self.x = x
        self.y = y
        self.Reset(self, False)
        return True