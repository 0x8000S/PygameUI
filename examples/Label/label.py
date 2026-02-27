import PygameUI
import pygame

# 作者: 氢気氚
# 标签组件演示
# 你可以导航到项目根目录，运行 `python -m examples.Label.label`

screen = pygame.display.set_mode((800, 600))

# 创建标签组件
label = PygameUI.widget.Label.Label("Hello,World!", 24, 100, 100)
# 参数从左到右依次是：标签显示文本、字体大小、X坐标、Y坐标

# 事件绑定演示
def LabelEvent(w:PygameUI.widget.Label.Label):
    print("Hello!")
    # 形参w为绑定的组件
    w.text = "Hola mundo!" # 改显示文本为 Hola mundo!
    # 你可以使用 w 来改改组件的内部变量
    w.theme_font_color = (255, 255, 255) # 改字体颜色为白色
    w.font_size = 40 # 改字体大小为40号
label.When(PygameUI.widget.Label.WidgetEvent.MouseIn, LabelEvent)
# 使用方法 When 来绑定事件，有两个参数
# 第一个参数为：事件名称，事件名称在PygameUI.widget.<组件名>.WidgetEvent的枚举中
# 参数二为绑定的函数
# 在本演示中，将标签的光标进入事件绑定到函数LabelEvent上
# 一个事件可以有多个绑定

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 不可直接调用 pygame.quit()，pygame会报错，需退出循环后调用
        PygameUI.HandleEvent(event)
    screen.fill((25, 45, 60))
    # 需先调用绘制函数，再调用更新函数，否则pygame会报错
    PygameUI.Draw(screen) # 为所有组件调用方法Draw(绘制)
    PygameUI.Update() # 为所有组件调用方法Update(更新)
    # PygameUI.Draw(screen) 和 PygameUI.Update() 均为简便写法，等价于如下两行
    # PygameUI.widget.Widget.WidgetManage.Draw(screen)
    # PygameUI.widget.Widget.WidgetManage.Update()
    pygame.display.flip()
pygame.quit()