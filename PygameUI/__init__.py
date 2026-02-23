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