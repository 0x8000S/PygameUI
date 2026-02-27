import pygame
from typing import Tuple
from enum import Enum

class FontSize(Enum):
    Small=18
    Median=20
    Big=24
    Large=28

Color = Tuple[int, int, int]

class ThemeData:
    def __init__(self, MainColor:Color, SubColor:Color,HoverColor:Color, BorderColor:Color, BorderHoverColor:Color):
        self.MainColor = MainColor
        self.SubColor = SubColor
        self.HoverColor = HoverColor
        self.BorderColor = BorderColor
        self.BorderHoverColor = BorderHoverColor
class ThemeFontData:
    def __init__(self, AFontName:str, AFontSize:int|FontSize, FontColor:Color):
        pygame.init()
        self.FontName = AFontName
        self.FontSize = None
        if isinstance(AFontSize, int):
            self.FontSize = AFontSize
        elif isinstance(AFontSize, FontSize):
            self.FontSize = AFontSize.value
        self.FontColor = FontColor
    def ChangeSize(self, Size:int|FontSize):
        if isinstance(Size, int):
            self.FontSize = Size
        elif isinstance(Size, FontSize):
            self.FontSize = Size.value
    def ChangeFont(self, font_file:str):
        self.FontName = font_file, self.FontSize
    def GetFont(self) -> pygame.font.Font:
        return pygame.font.SysFont(self.FontName, self.FontSize)

class Theme:
    def __init__(self, Data:ThemeData, Font:ThemeFontData):
        self.Data = Data
        self.Font = Font
    def GetConfig(self) -> Tuple[ThemeData, ThemeFontData]:
        return (self.Data, self.Font)

DefaultTheme:Theme