import vgamepad as vgp
import keyboard as kbd

print("GAMEPAD PHAKER by luRaichu (c) 2024")
joy = vgp.VX360Gamepad()
print("Emulated controller created!")
while True:
	# there's probably a cleaner and more efficient way to write this shit but HEHEHE it works
	if kbd.is_pressed('z') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_A)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_A)

	if kbd.is_pressed('x') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_B)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_B)

	if kbd.is_pressed('a') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_X)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_X)

	if kbd.is_pressed('s') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_Y)

	if kbd.is_pressed('up') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

	if kbd.is_pressed('down') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

	if kbd.is_pressed('left') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

	if kbd.is_pressed('right') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

	if kbd.is_pressed('enter') == True:
		joy.press_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_START)
	else:
		joy.release_button(button=vgp.XUSB_BUTTON.XUSB_GAMEPAD_START)

	joy.update()
