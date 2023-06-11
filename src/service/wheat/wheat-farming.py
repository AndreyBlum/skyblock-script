import pyautogui
import time

def harvest_wheat(direction):
    pyautogui.keyDown("x")
    print(direction)
    if direction == "right":
        move_to_right()
    else:
        move_to_left()
    time.sleep(90)
    direction = "left"
    if direction == "left":
        move_to_left()
    else:
        move_to_right()
    # Time to harvest all row
    time.sleep(90)
    direction = "right"
    return direction

def move_to_left():
    pyautogui.keyUp("D")
    pyautogui.keyDown("A")

def move_to_right():
    pyautogui.keyUp("A")
    pyautogui.keyDown("D")

def warp_garden():
    pyautogui.press("z")

def move_180():
    print("Moving 180 dregrees")
    pyautogui.move(800, 0)
    pyautogui.move(400, 0)
    pyautogui.keyDown("W")
    time.sleep(0.5)
    pyautogui.keyUp("W")
    
def change_window():
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('esc')

def locate_breaking_events():
    bad_internet = pyautogui.locateCenterOnScreen("src/assets/wheat/bad_internet.png", confidence=0.5)
    if bad_internet:
        print("Bad Internet - Exiting...")
        exit()

def act():
    runs = 0
    row_count = 0
    while(True):
        if runs == 0:
            change_window()
        locate_breaking_events()
        direction = "right"
        if row_count == 4:
            direction = "right"
            row_count = 0
            warp_garden()
        if row_count == 2:
            direction = "left"
            warp_garden()
            move_180()
        direction = harvest_wheat(direction)
        row_count += 1
        runs += 1
        print(f'You are in a {row_count}th row')
        print(f'You are in the run number {runs}')

act()   