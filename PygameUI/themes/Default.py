from . import Theme

Font = Theme.ThemeFontData('微软雅黑', Theme.FontSize.Median, (1,1,1))
Colors = Theme.ThemeData((37,99,235), (100,116,139), (59,103,246), (0,0,0), (255,255,255))

DTheme = Theme.Theme(Colors, Font)