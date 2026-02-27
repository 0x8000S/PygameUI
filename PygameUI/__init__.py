import sys
from tkinter import messagebox

try:
    import pygame
except ImportError:
    messagebox.showerror(
        "Missing Dependency",
        "PygameUI requires pygame.\n"
        "Please run: pip install pygame"
    )
    sys.exit(1)

from . import widget
from . import utils
from . import themes
from . import container

def HandleEvent(event:pygame.event.Event):
    widget.Widget.WidgetManage.HandleEvent(event)

def Update():
    widget.Widget.WidgetManage.Update()

def Draw(surface:pygame.surface.Surface):
    widget.Widget.WidgetManage.Draw(surface)
