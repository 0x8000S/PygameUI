import PygameUI
import pygame

# 作者: 氢気氚 (我的英文水平还算凑活吧)
# This is a show button widget's example file
# You can cd to the project root path, and run `python -m examples.button` command.

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a button
btn = PygameUI.widget.Button.Button("Hello!", 24, 40, 40, '', '', True, 2)
# The args from left to right, is text, font size, position x, position y, button width, button height, has border, border size.
# If width or height is str, The button's width or height will auto-calc.

# An event binding example
def WhenBtnIsClicked(w:PygameUI.widget.Button.Button):
    # The arg 'w' is your binding button
    print(f"The button {w.GetText()} was clicked!")
    # Can use arg 'w' to change button's inner variable
    w.text.font_size = 40
btn.When(PygameUI.widget.Button.WidgetEvent.Click, WhenBtnIsClicked)
# Use When method, binding event, 
# First arg, An event name, Use enum to save events, 
# Second arg, will binding on the function
# Every widget has a enum named WidgetEvent, You can use this to fill arg
# In this example, the button's click event to binding function
# One event can bind various function

running:bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Can't call pygame.quit(), Else pygame will raise error, You must exit this loop, Then call pygame.quit()
        PygameUI.widget.Widget.WidgetManage.HandleEvent(event)
    screen.fill((25, 45, 60))
    # The draw must before update, Else pygame will raise error
    
    PygameUI.widget.Widget.WidgetManage.Draw(screen) # For all based on widgets to call Draw method.
    PygameUI.widget.Widget.WidgetManage.Update()# For all based on widgets to call Update method.
    pygame.display.flip()

pygame.quit()