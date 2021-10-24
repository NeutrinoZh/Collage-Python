import winsound
import keyboard

duration = 100

def sound(e):
    global duration
    if e.name == '1':
        winsound.Beep(500, duration)
    elif e.name == '2':
        winsound.Beep(523, duration)
    elif e.name == '3':
        winsound.Beep(587, duration)
    elif e.name == '4':
        winsound.Beep(659, duration)
    elif e.name == '5':
        winsound.Beep(698, duration)
    elif e.name == '6':
        winsound.Beep(783, duration)
    elif e.name == '7':
        winsound.Beep(880, duration)
    elif e.name == '8':
        winsound.Beep(987, duration)

keyboard.hook(sound)
keyboard.wait('Ctrl + Q')