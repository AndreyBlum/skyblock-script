import pyautogui
import time

def harvest_mushroom(direction, row):
    pyautogui.keyDown("x")
    if row == 3:
        pyautogui.keyUp("D")
        warp_garden()
        move_180()
        direction = "left"
    if row == 6:
        warp_garden()
        return {
            "direction": "right",
            "row": 0,
        }
    print(direction)
    if row > 0:
        look_to_direction(invert_move(direction))
    move_to_direction(direction)
    row = row + 1
    print(f'You are in a {row}th row')
    time.sleep(70)
    return {
        "direction": invert_move(direction),
        "row": row,
    }

def move_to_left():
    pyautogui.keyUp("D")
    pyautogui.keyDown("A")

def move_to_right():
    pyautogui.keyUp("A")
    pyautogui.keyDown("D")

def move_to_direction(direction):
    if direction == "right":
        move_to_right()
    else:
        move_to_left()

def warp_garden():
    pyautogui.press("z")
    time.sleep(5)

def look_to_direction(direction):
    if direction == "right":
        look_right()
    else:
        look_left()

def look_right():
    pyautogui.move(120, 0)

def look_left():
    pyautogui.move(-120, 0)

def move_180():
    print("Moving 180 dregrees")
    pyautogui.move(800, 0)
    pyautogui.move(400, 0)
    pyautogui.keyDown("W")
    time.sleep(0.2)
    pyautogui.keyUp("W")

def invert_move(direction):
    pyautogui.keyDown("W")
    time.sleep(0.2)
    pyautogui.keyUp("W")
    if direction == "right":
        print("Inverted to left")
        return "left"
    else:
        print("Inverted to right")
        return "right"
def change_window():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)
    pyautogui.press('esc')

def locate_breaking_events():
    bad_internet = pyautogui.locateCenterOnScreen("src/assets/wheat/bad_internet.png", confidence=0.5)
    bad_internet_2 = pyautogui.locateCenterOnScreen("src/assets/wheat/bad_internet_2.png", confidence=0.5)
    if bad_internet or bad_internet_2:
        print("Bad Internet - Exiting...")
        exit()
    warped_to_hub = pyautogui.locateCenterOnScreen("src/assets/wheat/warped_to_hub.png")
    warped_to_hub_2 = pyautogui.locateCenterOnScreen("src/assets/wheat/warped_to_hub_2.png")
    if warped_to_hub or warped_to_hub_2:
        print("You got warped to hub - Warping back Garden...")
        warp_garden()

def act():
    runs = 0
    row_count = 0
    direction = "right"
    while(True):
        if runs == 0:
            change_window()
            runs += 1
        locate_breaking_events()
        print(row_count)
        harvesting = harvest_mushroom(direction, row_count)
        print(harvesting)
        try:
            direction = harvesting["direction"]
            row_count = harvesting["row"]
        except Exception as err:
            print(f"Value not found: {err}")
        print(f"This is the direction {direction} and the row_count {row_count}")
        print(f'You are in the run number {runs}')

act()
