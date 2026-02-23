import sys
from . import widget
from . import utils
from . import themes
from . import container
from tkinter import messagebox


try:
    import pygame
except ImportError:
    try:
        from tkinter import messagebox
        messagebox.showerror(
            "Missing Dependency",
            "PygameUI requires pygame.\n"
            "Install: pip install pygame"
        )
    except Exception:
        print("Error: PygameUI requires pygame.")
        print("Install: pip install pygame")
    
    sys.exit(1)