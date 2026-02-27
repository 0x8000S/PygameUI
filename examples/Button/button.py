import PygameUI
import pygame

# 作者: 氢気氚
# 按钮组件演示
# 你可以导航到项目根目录，运行 `python -m examples.Button.button`

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 创建按钮
btn = PygameUI.widget.Button.Button("Hello!", 24, 40, 40, '', '', True, 2)
# 参数从左至右分别为：按钮文本、字体大小、X坐标、Y坐标、按钮宽度、按钮高度、是否有边框、边框大小
# 当按钮大小参数类型为字符串时，按钮的大小将会自动计算

# 事件绑定演示
def WhenBtnIsClicked(w:PygameUI.widget.Button.Button):
    # 形参w为绑定的组件
    print(f"The button {w.GetText()} was clicked!")
    # 你可以使用 w 来改改组件的内部变量
    w.text.font_size = 40
    w.text.theme_font_color = (255,255,255)
    w.border_width = 6
btn.When(PygameUI.widget.Button.WidgetEvent.Click, WhenBtnIsClicked)
# 使用方法 When 来绑定事件，有两个参数
# 第一个参数为：事件名称，事件名称在PygameUI.widget.<组件名>.WidgetEvent的枚举中
# 参数二为绑定的函数
# 在本演示中，将按钮的点击事件绑定到函数WhenBtnIsClicked上
# 一个事件可以有多个绑定

running:bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 不可直接调用 pygame.quit()，pygame会报错，需退出循环后调用
        PygameUI.widget.Widget.WidgetManage.HandleEvent(event)
    screen.fill((25, 45, 60))
    # 需先调用绘制函数，再调用更新函数，否则pygame会报错
    PygameUI.widget.Widget.WidgetManage.Draw(screen) # 为所有组件调用方法Draw(绘制)
    PygameUI.widget.Widget.WidgetManage.Update() # 为所有组件调用方法Update(更新)
    pygame.display.flip()

pygame.quit()