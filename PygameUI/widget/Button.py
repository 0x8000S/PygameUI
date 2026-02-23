import pygame
from .. import themes
from . import Widget
from ..utils import EqEventFunction
from enum import Enum

class WidgetEvent(Enum):
    MouseIn='MouseIn',
    MouseExit='MouseExit',
    Hover='Hover',
    MouseDown='MouseDown',
    MouseUp='MouseUp',
    Click='Click'

class Button(Widget.Widget):
    Events = WidgetEvent
    def __init__(self, text:str, font_size:int|Widget.themes.Theme.FontSize, x:int, y:int, width:int|str, height:int|str, border:bool, border_width:int, parent = None):
        super().__init__(x, y, width, height, parent)
        self._text = text
        self.border = border
        self.border_width = border_width
        self._font_size = font_size
        self.theme.Font.ChangeSize(font_size)
        self.theme_background_color = self.theme.Data.MainColor
        self.theme_border_color = self.theme.Data.BorderColor
        self._theme_font_color = self.theme.Font.FontColor
        self.font_image = self.theme.Font.Font.render(self.text, True, self.theme_font_color)
        self._auto_width:bool = False
        self._auto_height:bool = False
        self.font = self.font_image.get_rect()
        if isinstance(self.width, str):
            self.width = self.font.width+10
            self._auto_width = True
        if isinstance(self.height, str):
            self.height = self.font.height+10
            self._auto_height = True
        self.background_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.border_rect = pygame.rect.Rect(self.x-self.border_width, self.y-self.border_width, self.width+self.border_width*2, self.height+self.border_width*2)
        self.font.topleft = (self.background_rect.x+self.background_rect.width/2-self.font.width/2, self.background_rect.y+self.background_rect.height/2-self.font.height/2)
        self.When(self.cevent.MouseIn, self._MouseInEvent)
        self.When(self.cevent.MouseExit, self._MouseExitEvent)
    @property
    def font_size(self):
        return self._font_size
    @font_size.setter
    def font_size(self, val):
        self._font_size = val
        self.theme.Font.ChangeSize(self.font_size)
        self.ChangeText()
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, val):
        self._text = val
        self.ChangeText()
    def ChangeText(self):
        self.ChangeFontColor()
        if self._auto_width:
            self.width = self.font.width+10
        if self._auto_height:
            self.height = self.font.height+10
        self.background_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.border_rect = pygame.rect.Rect(self.x-self.border_width, self.y-self.border_width, self.width+self.border_width*2, self.height+self.border_width*2)
        self.font.topleft = (self.background_rect.x+self.background_rect.width/2-self.font.width/2, self.background_rect.y+self.background_rect.height/2-self.font.height/2)
        
    @property
    def theme_font_color(self):
        return self._theme_font_color
    @theme_font_color.setter
    def theme_font_color(self, val):
        self._theme_font_color = val
        self.ChangeFontColor()
    def ChangeFontColor(self):
        self.font_image = self.theme.Font.Font.render(self.text, True, self.theme_font_color)
        self.font = self.font_image.get_rect()
        self.font.topleft = (self.background_rect.x+self.background_rect.width/2-self.font.width/2, self.background_rect.y+self.background_rect.height/2-self.font.height/2)
    def _MouseInEvent(self, w):
        self.theme_border_color = self.theme.Data.BorderHoverColor
    def _MouseExitEvent(self, w):
        self.theme_border_color = self.theme.Data.BorderColor
    def HandleEvent(self, event):
        if not super().HandleEvent(event):
            return False
        if self._MouseIn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.Emit(self.cevent.Click)
                    self.Emit(self.cevent.MouseDown)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.Emit(self.cevent.MouseUp)
        return True
    def Update(self):
        if super().Update():
            return False
        
        return True
    def Draw(self, surface:pygame.surface.Surface):
        if not super().Draw(surface):
            return False
        pygame.draw.rect(surface, self.theme_border_color, self.border_rect)
        pygame.draw.rect(surface, self.theme_background_color, self.background_rect)
        surface.blit(self.font_image, (self.font.x, self.font.y))
        
        return True
    