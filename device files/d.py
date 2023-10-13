import display
import time

# Hello world と その下に白い線を表示
text = display.Text('Hello world', 320, 200, display.WHITE, justify=display.MIDDLE_CENTER)
line = display.Line(175, 230, 465, 230, display.WHITE)
display.show(text, line)

time.sleep(3)

# group に text と line を入れて、緑色に変えて表示
group = [text, line]
display.color(group, display.GREEN)
display.show(group)

time.sleep(3)


# lineを上に75px移動して表示
display.move(line, 0, -75)
# line.move(0, -75)
display.show(group)

time.sleep(3)

# Create a white polygon with a red outline and print everything again
poly = display.Polygon([0, 0, 639, 399, 0, 399], display.WHITE)
outline = display.Polyline([0, 0, 639, 399, 0, 399, 0, 0], display.RED)
display.show(group, outline, poly)
