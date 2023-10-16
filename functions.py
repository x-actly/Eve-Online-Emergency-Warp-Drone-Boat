import keyboard, time, datetime, random
import pyautogui





def emergency_warp(x, y):

    random_time = random.uniform(1,2)
    y_offset_align = random.randint(77, 79)
    y_offset_warp = random.randint(-51,-49)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # console
    print(f"[{timestamp}] - emergency warp...")
    # warp to belt
    for i in range(1):


        ######### drones in #########
        # time.sleep(1)
        # pyautogui.keyDown('shift')
        # pyautogui.press('r')
        # time.sleep(1)
        # pyautogui.keyUp('shift')
        # time.sleep(5)
        ######### align #############
        time.sleep(random_time)
        pyautogui.press('f3')
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(random_time)
        pyautogui.moveRel(-45, y_offset_align, 1)
        pyautogui.mouseUp()
        time.sleep(5)
        ######### warp ############## 
        #time.sleep(random_time)
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(random_time)
        pyautogui.moveRel(-50, y_offset_warp, 1)
        pyautogui.mouseUp()
    