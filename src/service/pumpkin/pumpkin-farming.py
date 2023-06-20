import pyautogui
import time

def harvest_pumpkin(direction, row):
    pyautogui.keyDown("x")
    if row == 3:
        move_to_next_pumpkin_crops()
    if row == 4:
        get_first_upstairs()
    if row == 5:
        get_second_upstairs()
    if row == 6:
        warp_garden()
        return {
            "direction": "left",
            "row": 0,
        }
    print(direction)
    move_to_direction(direction)
    row = row + 1
    print(f'You are in a {row}th row')
    time.sleep(50)
    return {
        "direction": invert_move(direction),
        "row": row,
    }

def move_to_next_pumpkin_crops():
    pyautogui.keyUp("A")
    pyautogui.keyDown("S")
    time.sleep(2)
    pyautogui.keyUp("S")
    move_to_right()
    time.sleep(0.1)
    pyautogui.keyUp("D")
    pyautogui.keyDown("W")
    time.sleep(0.1)
    pyautogui.keyUp("W")

def get_first_upstairs():
    pyautogui.keyUp("D")
    move_to_front()
    pyautogui.keyDown("A")
    time.sleep(0.5)
    pyautogui.keyUp("A")
    move_to_back()
    move_to_left()
    time.sleep(0.05)
    pyautogui.keyUp("A")
    move_to_front()

def get_second_upstairs():
    pyautogui.keyUp("A")
    move_to_front()
    pyautogui.keyDown("D")
    time.sleep(0.5)
    pyautogui.keyUp("D")
    move_to_back()
    move_to_right()
    time.sleep(0.05)
    pyautogui.keyUp("D")
    pyautogui.keyUp("A")
    move_to_front()

def move_to_left():
    pyautogui.keyUp("D")
    pyautogui.keyDown("A")

def move_to_right():
    pyautogui.keyUp("A")
    pyautogui.keyDown("D")

def move_to_front():
    pyautogui.keyDown("W")
    time.sleep(0.1)
    pyautogui.keyUp("W")

def move_to_back():
    pyautogui.keyDown("D")
    time.sleep(0.5)
    pyautogui.keyUp("D")

def move_to_direction(direction):
    if direction == "right":
        move_to_right()
    else:
        move_to_left()

def warp_garden():
    pyautogui.press("z")
    time.sleep(5)

def invert_move(direction):
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
    direction = "left"
    while(True):
        if runs == 0:
            change_window()
            runs += 1
        locate_breaking_events()
        print(row_count)
        harvesting = harvest_pumpkin(direction, row_count)
        print(harvesting)
        try:
            direction = harvesting["direction"]
            row_count = harvesting["row"]
        except Exception as err:
            print(f"Value not found: {err}")
        print(f"This is the direction {direction} and the row_count {row_count}")
        print(f'You are in the run number {runs}')

act()