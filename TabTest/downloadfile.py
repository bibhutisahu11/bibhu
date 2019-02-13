import pyautogui as ptg
import time
import datetime
ptg.PAUSE = 1


def find_and_click(image_name, clicks=1, interval=1, x_offset=0,y_offset=0, button="left"):
    image_path = image_folder + "\\" + image_name + ".png"
    #noinspection PyBroadException
    try:
        coords = ptg.locateCenterOnScreen(image_path)
        ptg.click(x=coords[0] + x_offset, y=coords[1] + y_offset, clicks=clicks, interval=interval, button=button)
    except:
        time.sleep(3)
        coords = ptg.locateCenterOnScreen(image_path)
        ptg.click(x=coords[0] + x_offset, y=coords[1] + y_offset, clicks=clicks, interval=interval, button=button)


image_folder = r'C:\Users\sahubi2\Documents\automation'


def check_results_exist():
    image_path = image_folder + "\\" + "no_search_results.png"
    # coords=ptg.locateCenterOnScreen(image_path)
    coords = None

    if coords is None:
        print("just before return", datetime.datetime.time(datetime.datetime.now()))
        return True
    else:
        return False




