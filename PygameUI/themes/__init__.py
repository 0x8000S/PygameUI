from . import Theme


def GetDefaultTheme() -> Theme.Theme:
    from . import Default
    return Default.DTheme