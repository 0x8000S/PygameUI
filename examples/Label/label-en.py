import PygameUI
import pygame

# 作者: 氢気氚
# Widget Label example
# You can cd to the project root path, and run `python -m examples.Label.label-en` command.

screen = pygame.display.set_mode((800, 600))

# Create a label
label = PygameUI.widget.Label.Label("Hello,World!", 24, 100, 100)
# The args from left to right, is text, font size, position x, position y

# An event binding example
def LabelEvent(w:PygameUI.widget.Label.Label):
    print("Hello!")
    # The arg 'w' is your binding label
    w.text = "Hola mundo!"
    # Can use arg 'w' to change label's inner variable
    w.theme_font_color = (255, 255, 255)
    w.font_size = 40
label.When(PygameUI.widget.Label.WidgetEvent.MouseIn, LabelEvent)
# Use When method, binding event, 
# First arg, An event name, Use enum to save events, 
# Second arg, will binding on the function
# Every widget has a enum named WidgetEvent, You can use this to fill arg
# In this example, the button's click event to binding function
# One event can bind various function

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Can't call pygame.quit(), Else pygame will raise error, You must exit this loop, Then call pygame.quit()
    screen.fill((25, 45, 60))
    # The draw must before update, Else pygame will raise error
    PygameUI.Draw(screen) # For all based on widgets to call Draw method.
    PygameUI.Update() # For all based on widgets to call Update method.
    # PygameUI.Draw(screen) and PygameUI.Update() is a simple function, it's equivalent
    # PygameUI.widget.Widget.WidgetManage.Draw(screen)
    # PygameUI.widget.Widget.WidgetManage.Update()
    pygame.display.flip()
pygame.quit()