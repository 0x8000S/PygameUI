from enum import Enum
import pygame
from . import Widget


class WidgetEvent(Enum):
    MouseIn='MouseIn'
    MouseExit='MouseExit'
    Hover='Hover'
    Update='Update'

class Label(Widget.Widget):
    Events = WidgetEvent
    def __init__(self, text, font_size, x, y, theme=None):
        super().__init__(x, y, 0, 0, theme)
        self._text = text
        self._font_size = font_size
        self._theme_font_color = self.theme.Font.FontColor
        self.theme.Font.ChangeSize(font_size)
        self.font_image = self.theme.Font.GetFont().render(self.text, True, self.theme_font_color)
        self.font = self.font_image.get_rect()
        self.font.topleft = (x, y)
        self.width = self.font.width
        self.height = self.font.height
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
        
        self.width = self.font.width
        self.height = self.font.height
        self.font.topleft = (self.x, self.y)
        self.ReflashFont()
    def GetRect(self) -> pygame.rect.Rect:
        return self.font
    @property
    def theme_font_color(self):
        return self._theme_font_color
    @theme_font_color.setter
    def theme_font_color(self, val):
        self._theme_font_color = val
        self.ReflashFont()
    def LoadFontFile(self, font_file:str):
        self.theme.Font.ChangeFont(font_file)
        self.ReflashFont()
    def ReflashFont(self):
        self.font_image = self.theme.Font.GetFont().render(self.text, True, self.theme_font_color)
        self.font = self.font_image.get_rect()
        self.font.topleft = (self.x, self.y)
        self.width = self.font.width
        self.height = self.font.height
        self.Emit(self.cevent.Update)
    def HandleEvent(self, event) -> bool:
        if not super().HandleEvent(event):
            return False
        
        return True
    def Update(self) -> bool:
        if not super().Update():
            return False
        
        return True
    def Draw(self, surface:pygame.surface.Surface) -> bool:
        if not super().Draw(surface):
            return False
        surface.blit(self.font_image, (self.font.x, self.font.y))
        return True
    def Move(self, x, y):
        if not super().Move(x,y):
            return False
        self.font.topleft = (x, y)
        return True