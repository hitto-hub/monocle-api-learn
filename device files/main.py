import random
import display
import time
import touch
import device
display.brightness(3)
def fn():
    global f
    global battery
    print(touch.state())
    if f == 0:
        quiz()
        while (True):
            if touch.state(touch.EITHER):
                print("1")
                break
        fn()
    elif f == 2:
        global sum
        global f
        f = 0
        sum = str(sum)
        sub = display.Text('ANSWER', 320, 140, display.GREEN, justify=display.MIDDLE_CENTER)
        text = display.Text(sum, 320, 200, display.GREEN, justify=display.MIDDLE_CENTER)
        display.show(text, sub, battery)
        t = time.ticks_ms()
        while (True):
            if touch.state(touch.EITHER) and t + 1000 < time.ticks_ms():
                print("2")
                break
        fn()
def bold(num, sec):
    global battery
    width = 1
    timeout = time.ticks_ms() + sec * 1000
    while True:
        text = display.Text(num, 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        text = display.Text(num, 320 + width, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        text = display.Text(num, 320, 200 + width, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        text = display.Text(num, 320 + width, 200 + width, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        if time.ticks_ms() >= timeout:
            break
def quiz():
    global sum
    global f
    global battery
    sum = 0
    f = 1
    battery = display.Text(str(device.battery_level()), 0, 0, display.WHITE, justify=display.TOP_LEFT)
    timeout = time.ticks_ms() + 1 * 1000
    while True:
        text = display.Text("3..", 260, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        if time.ticks_ms() >= timeout:
            break
    timeout = time.ticks_ms() + 1 * 1000
    while True:
        text = display.Text("2..", 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        if time.ticks_ms() >= timeout:
            break
    timeout = time.ticks_ms() + 1 * 1000
    while True:
        text = display.Text("1..", 380, 200, display.WHITE, justify=display.MIDDLE_CENTER)
        display.show(text, battery)
        if time.ticks_ms() >= timeout:
            break
    bold("start!", 1)
    global tmp
    for i in range(3):
        while True:
            num = int(random.randint(1, 5))
            if num != tmp:
                tmp = num
                break
        sum += num
        num = str(num)
        bold(num, 1)
    sub = display.Text('Thinking...', 320, 140, display.WHITE, justify=display.MIDDLE_CENTER)
    text = display.Text('touch to display answer', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
    display.show(text, sub, battery)
    f = 2
f = 0
battery = display.Text(str(device.battery_level()), 0, 0, display.WHITE, justify=display.TOP_LEFT)
text = display.Text('touch to start', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
display.show(text, battery)
tmp = 0
while (True):
    print(touch.state(touch.EITHER))
    if touch.state(touch.EITHER):
        print("3")
        break
fn()