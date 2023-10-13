import camera
import bluetooth

# Capture a JPEG image and transfer it over the Bluetooth raw data service
camera.capture()
# print(chr(int(camera.read(), 16)))
print(camera.read())


# Capture a JPEG image and transfer it over the Bluetooth raw data service
while data := camera.read(bluetooth.max_length()):
    bluetooth.send(data)



