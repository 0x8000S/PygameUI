# PygameUI API Reference

PygameUI 是一个基于 Pygame 的轻量级 GUI 框架，提供组件化、事件驱动的 UI 开发体验。

---

## 目录

- [utils.Pos](#utilspos) — 几何工具
- [themes](#themes) — 主题系统
- [widget.Widget](#widgetwidget) — 组件基类
- [widget.Label](#widgetlabel) — 文本组件
- [widget.Button](#widgetbutton) — 按钮组件

---

## utils.Pos

基础几何类型和碰撞检测。

### Position(x, y)

二维坐标点。

| 属性  | 类型    | 说明   |
| ----- | ------- | ------ |
| `x` | `int` | X 坐标 |
| `y` | `int` | Y 坐标 |

### Area(x, y, width, height)

矩形区域。

| 属性       | 类型    | 说明     |
| ---------- | ------- | -------- |
| `x`      | `int` | 左上角 X |
| `y`      | `int` | 左上角 Y |
| `width`  | `int` | 宽度     |
| `height` | `int` | 高度     |

### CheckPosInArea(area, pos) -&gt; bool

检测点是否在区域内（包含边界）。

```python
from PygameUI.utils.Pos import Position, Area, CheckPosInArea

area = Area(100, 100, 80, 40)
pos = Position(120, 120)
if CheckPosInArea(area, pos):
    print("Inside")
```


## themes

视觉样式配置系统。

### FontSize(Enum)

预定义字体大小。

**表格**

| 成员       | 值 |
| :--------- | :- |
| `Small`  | 18 |
| `Median` | 20 |
| `Big`    | 24 |
| `Large`  | 28 |

### ThemeData(MainColor, SubColor, HoverColor, BorderColor, BorderHoverColor)

颜色配置数据类。

### ThemeFontData(AFontName, AFontSize, FontColor)

字体配置数据类。

**表格**

| 属性          | 说明                      |
| :------------ | :------------------------ |
| `FontName`  | 系统字体名称              |
| `FontSize`  | 当前大小（整数）          |
| `Font`      | `pygame.font.Font` 实例 |
| `FontColor` | RGB 颜色                  |

 **方法** :

* `ChangeSize(Size: int | FontSize)` — 修改字体大小
* `ChangeFont(font_file: str)` — 切换字体（注：当前实现仍使用 SysFont）

### Theme(Data, Font)

主题容器，包含颜色和字体配置。

**Python**

```python
from PygameUI import themes

data = themes.ThemeData(
    MainColor=(240, 240, 240),
    SubColor=(220, 220, 220),
    HoverColor=(200, 200, 255),
    BorderColor=(100, 100, 100),
    BorderHoverColor=(50, 100, 200)
)

font = themes.ThemeFontData("Arial", themes.FontSize.Median, (0, 0, 0))
my_theme = themes.Theme(data, font)
```

---

## widget.Widget

所有 UI 组件的抽象基类。

### WidgetManage

全局组件管理器（单例模式）。

**表格**

| 类方法                 | 说明               |
| :--------------------- | :----------------- |
| `HandleEvent(event)` | 向所有组件广播事件 |
| `Update()`           | 更新所有组件       |
| `Draw(surface)`      | 绘制所有组件       |

### Widget(x, y, width, height, parent=None)

 **参数** :

* `x, y`: 左上角坐标
* `width, height`: 尺寸
* `parent`: 父组件（可选）

 **核心属性** :

* `visible: bool` — 是否可见
* `enable: bool` — 是否启用
* `theme: Theme` — 当前主题

 **事件系统** :

**表格**

| 方法                  | 说明                   |
| :-------------------- | :--------------------- |
| `When(event, func)` | 绑定事件回调           |
| `Emit(event)`       | 触发事件               |
| `GetWidgetEvents()` | 获取事件枚举（类方法） |

 **基类事件** :

* `MouseIn` — 鼠标进入
* `MouseExit` — 鼠标离开
* `Hover` — 鼠标悬停

 **抽象方法** （子类必须实现）:

**Python**

```python
def Draw(self, surface: pygame.Surface) -> bool: ...
```

 **可重写方法** :

**Python**

```python
def HandleEvent(self, event) -> bool: ...
def Update(self) -> bool: ...
```

 **注意** : 重写时必须调用 `super()` 保持基础功能。

---

## widget.Label

纯文本显示组件，继承自 Widget。

### 扩展事件

* `Update` — 文本/字体/颜色变化时触发

### Label(text, font_size, x, y, parent=None)

 **属性** （修改后自动重渲染）:

**表格**

| 属性                 | 类型      | 说明     |
| :------------------- | :-------- | :------- |
| `text`             | `str`   | 文本内容 |
| `font_size`        | `int`   | 字体大小 |
| `theme_font_color` | `Color` | 字体颜色 |

 **方法** :

**表格**

| 方法                        | 返回值          | 说明         |
| :-------------------------- | :-------------- | :----------- |
| `GetRect()`               | `pygame.Rect` | 获取文本矩形 |
| `LoadFontFile(font_file)` | `None`        | 加载字体文件 |

**Python**

```python
from PygameUI.widget import Label

label = Label("Hello", 24, 100, 100)
label.text = "World"  # 自动触发重渲染
label.font_size = 36
```

---

## widget.Button

可点击按钮组件，继承自 Widget。

### 扩展事件

* `MouseDown` — 鼠标按下
* `MouseUp` — 鼠标释放
* `Click` — 点击完成

### Button(text, font_size, x, y, width, height, border, border_width, parent=None)

 **参数** :

* `text`: 按钮文本
* `font_size`: 字体大小
* `x, y`: 位置
* `width, height`: 尺寸（字符串类型时自动计算）
* `border`: 是否显示边框
* `border_width`: 边框宽度

 **自动尺寸** : `width` 或 `height` 传字符串时，根据文本 + 10px 内边距自动计算。

 **方法** :

**表格**

| 方法               | 返回值   | 说明                               |
| :----------------- | :------- | :--------------------------------- |
| `GetText()`      | `str`  | 获取当前文本                       |
| `ReflashText(w)` | `None` | 文本变化时重新计算布局（内部使用） |

**Python**

```python
from PygameUI.widget import Button

# 固定尺寸
btn = Button("OK", 24, 100, 100, 80, 40, True, 2)

# 自动尺寸
btn2 = Button("Cancel", 24, 200, 100, '', '', True, 2)

# 绑定点击
def on_click(button):
    print(f"Clicked {button.GetText()}")

btn.When(Button.Events.Click, on_click)
```

 **视觉结构** :

```plain
┌─────────────────┐  ← 外边框（border_rect）
│  ┌───────────┐  │
│  │   文本    │  │  ← 背景（background_rect）+ 文本
│  └───────────┘  │
└─────────────────┘
```

---

## 类型对照表

**表格**

| Python 类型                 | 实际含义                            |
| :-------------------------- | :---------------------------------- |
| `Color`                   | `Tuple[int, int, int]` — RGB     |
| `FontSize`                | `int` 或 `themes.FontSize` 枚举 |
| `Callable[[Widget], Any]` | 事件回调函数签名                    |

---

## 架构概览

```plain
PygameUI
├── utils/
│   └── Pos.py          # Position, Area, CheckPosInArea
├── themes.py           # FontSize, ThemeData, ThemeFontData, Theme
└── widget/
    ├── Widget.py       # Widget (基类), WidgetManage
    ├── Label.py        # Label (文本)
    └── Button.py       # Button (按钮)

用户主循环
    │
    ├── WidgetManage.HandleEvent(event)
    ├── WidgetManage.Update()
    └── WidgetManage.Draw(screen)
```
