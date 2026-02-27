import PygameUI
import pygame
import copy
pygame.init()

# 作者：氢気氚
# PygameUI项目组件演示
# 导航至当前项目的根目录，运行 `python -m examples.widgets`

PygameUI.themes.Default.DTheme.Font.FontColor = (255, 255, 255) # 设置默认主题的字体颜色
dts = copy.deepcopy(PygameUI.themes.GetDefaultTheme()) # 拷贝默认主题
dts.Font.FontColor = (164, 108, 140) # 设置拷贝主题的颜色

screen = pygame.display.set_mode((800, 600))
vbox = PygameUI.container.VBoxLayout.VBoxLayout(10, 10, 10) # 创建垂直布局管理器
hbox = PygameUI.container.HBoxLayout.HBoxLayout(0, 0, 10) # 创建横向布局管理器
title = PygameUI.widget.Label.Label("PygameUI模块UI演示!", 40,0,0) # 创建文本标签
lab = PygameUI.widget.Label.Label("我是标签", 30,0,0, dts) # 创建文本标签
btn = PygameUI.widget.Button.Button("我是按钮", 30, 0,0,'','',True, 4) # 创建按钮
cbox = PygameUI.widget.CheckBox.CheckBox("我是复选框", 0, 0) # 创建复选框组件
vbox.AddWidget(title) # 将标签加入垂直布局管理器
hbox.AddWidget(lab) # 将标签lab加入水平布局管理器
hbox.AddWidget(btn) # 将按钮加入水平布局管理器
vbox.AddWidget(hbox) # 将水平布局管理器加入垂直布局管理器
vbox.AddWidget(cbox) # 将复选框cbox加入垂直布局管理器

def WhenBtnClicked(w:PygameUI.widget.Button.Button):
    w.text.font_size = 80
    w.text.theme_font_color = (255, 144, 200)
    w.text.text = "Hola mundo!"

btn.When(PygameUI.widget.Button.WidgetEvent.Click, WhenBtnClicked)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        PygameUI.HandleEvent(event) # 传递事件
    screen.fill((25, 45, 60))
    PygameUI.Draw(screen) # 绘制
    PygameUI.Update() # 更新
    pygame.display.flip()
pygame.quit()