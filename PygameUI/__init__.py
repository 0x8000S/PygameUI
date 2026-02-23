import sys
from . import widget
from . import utils
from . import themes
from . import container


try:
    import pygame
except ImportError:
    print("Not found module pygame\nPlease run `pip install pygame`!")
    sys.exit(-1)