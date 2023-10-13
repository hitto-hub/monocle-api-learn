import random
import display
import time
import touch

class sta:
    sum = 0
    f = 0

s = sta()

# Define the touch callback function which is triggered upon a touch event
def fn(arg, s):
    if arg == touch.A:
        s.f = 1
        for i in range(5):
            num = int(random.randint(10, 100))
            s.sum += num
            num = str(num)
            text = display.Text(num, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
            line = display.Line(175, 230, 465, 230, display.WHITE)
            display.show(text, line)
            time.sleep(1)
        text = display.Text('touch L', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, line)
        s.f = 0

    if arg == touch.B:
        str_sum = str(s.sum)
        text = display.Text(str_sum, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, line)

text = display.Text("hi", 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
line = display.Line(175, 230, 465, 230, display.WHITE)
display.show(text, line)
print(s.f)
# if s.f == 0:
touch.callback(touch.EITHER, fn(touch.EITHER, s))