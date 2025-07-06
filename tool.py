import random
import threading
from time import sleep
from winotify import Notification
from pynput import mouse
import keyboard
import pyautogui
import toml

config = None
lock = threading.Lock()
pos = None
def switch():
    global pos
    with lock:
        if pos is None:
            Notification( app_id="Auto Clicker", title='', msg='左击一次开始连点', duration="short" ).show()
            listen_left()
        elif pos != 0:
            pos = None
            Notification( app_id="Auto Clicker", title='', msg='已停止连点', duration="short" ).show()

listener = None
def listen_left():
    global listener
    if listener is None:
       listener = mouse.Listener(on_click=on_click)
       listener.start()
       
def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        global pos, listener
        with lock:
            pos = (x, y)
            listener.stop()
            listener = None
            Notification( app_id="Auto Clicker", title='', msg=f"正在连点 {pos}", duration="short" ).show()

def click():
    global pos
    with lock:
        if pos is None: return
        curr_pos = pyautogui.position()
        offset_x = random.randint(-config['offset'], config['offset'])
        offset_y = random.randint(-config['offset'], config['offset'])
        pyautogui.moveTo(pos[0] + offset_x, pos[1] + offset_y)
        pyautogui.click()
        pyautogui.moveTo(curr_pos)

def clicker():
    global keep_sig, is_paused
    while keep_sig:
        sleep(random.uniform(config['speed'][0], config['speed'][1]))
        if not is_paused: click()

keep_sig = True
is_paused = False

def pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        Notification( app_id="Auto Clicker", title='', msg='已暂停连点', duration="short" ).show()
    else:
        Notification( app_id="Auto Clicker", title='', msg='已恢复连点', duration="short" ).show()

def quit():
    global keep_sig
    keep_sig = False

if __name__ == "__main__":
    with open('config.toml', 'r') as f:
        config = toml.load(f)

    t = threading.Thread(target=clicker)
    t.start()

    keyboard.add_hotkey(config['shortcut']['pause'], pause)
    keyboard.add_hotkey(config['shortcut']['swicth'], switch)
    keyboard.add_hotkey(config['shortcut']['exit'], quit)

    while keep_sig:
        sleep(0.1)