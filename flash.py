import random
import display
import time
import touch
# f = 0 起動時,答え表示中
# f = 1 問題表示中
# f = 2 答え表示待ち

display.brightness(3)

def fn(arg):
    global f
    print(touch.state())
    # 右
    if arg == touch.A:
        if f != 0:
            return
        quiz()
    # 回答表示
    # 左
    if arg == touch.B:
        if f != 2:
            return
        global sum
        global f
        f = 0
        sum = str(sum)
        text = display.Text(sum, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text)


def bold(num, sec):
    width = 1
    timeout = time.time() + sec
    while True:
        print(f"timeout: {timeout}, time: {time.time()}")
        text = display.Text(num, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text)
        text = display.Text(num, 320 + width, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text)
        text = display.Text(num, 320, 200 + width, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text)
        text = display.Text(num, 320 + width, 200 + width, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text)
        if time.time() >= timeout:
            break
    # display.clear()

def quiz():
    global sum
    global f
    sum = 0
    f = 1
    bold("start!", 2)
    for i in range(5):
        num = int(random.randint(10, 100))
        sum += num
        num = str(num)
        bold(num, 1)
    text = display.Text('L button press is answer', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
    display.show(text)
    f = 2

f = 0
text = display.Text('R button press is start', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
display.show(text)

touch.callback(touch.EITHER, fn)
