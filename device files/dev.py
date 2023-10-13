import device
def info():
	print(f"version:{device.VERSION}") # Prints the device firmware version
	print(f"battery:{device.battery_level()}%") # Returns the current battery level as a percentage
