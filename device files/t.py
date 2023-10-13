import touch
def fn(arg):
    print(arg)
    print(f"touch.EITHER:{touch.EITHER}")
    if arg == touch.A:
        print("button A pressed!")
    if arg == touch.B:
        print("button B pressed!")
touch.callback(touch.EITHER, fn)