import random
import display
import time

sum = 0
for i in range(5):
    num = int(random.randint(1, 4))
    sum += num
    num = str(num)
    text = display.Text(num, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
    line = display.Line(175, 230, 465, 230, display.WHITE)
    display.show(text, line)
    time.sleep(3)

text = display.Text('end', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
display.show(text, line)
time.sleep(3)
sum = str(sum)
text = display.Text(sum, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
display.show(text, line)

# display.FONT_WIDTH = 36
# display.FONT_HEIGHT = 48
