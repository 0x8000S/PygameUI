from .Theme import Theme


def GetDefaultTheme() -> Theme:
    from . import Default
    return Default.DTheme