#%%
import pyautogui
from time import localtime

pyautogui.FAILSAFE = True

def run_mouse_clicker():
    """Takes user input in military time to run mouse clicks until desired time is reached"""
    stop_at = [int(i) for i in input('military hour and minute: ').split(',')]

    while localtime().tm_hour != stop_at[0] or localtime().tm_min != stop_at[1]:
        pyautogui.doubleClick(x=1600, y=200, button='left')
        pyautogui.doubleClick(x=1500, y=300, button='left')
            
    print('Done:', localtime())

# %%
