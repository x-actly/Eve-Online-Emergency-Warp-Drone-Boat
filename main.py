import pyautogui, sys, random, time, pygame, time
from playsound import playsound
from datetime import datetime
from functions import emergency_warp

alarm_played = False

def find_and_execute(image_paths, action_function, start_x, start_y, end_x, end_y, confidence):
    search_region = (start_x, start_y, end_x - start_x, end_y - start_y)
    for image_path in image_paths:
        position = pyautogui.locateOnScreen(image_path, region=search_region, confidence=confidence)

        if position is not None:
            action_function()
            return True
    return False



def perform_action():
    global alarm_played
    if not alarm_played:
        pygame.mixer.init()
        pygame.mixer.music.load('sound/alarm.mp3')
        pygame.mixer.music.play()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"warping to safespot at {current_time}")
        while pygame.mixer.music.get_busy():
            continue
        alarm_played = True
        emergency_warp(1703, 1068)

    sys.exit()


start_x, start_y = 307, 704  
end_x, end_y = 476, 1307  
#image_paths = ['img/neut_4k.png', 'img/red_4k.png']  
image_paths = ['img/neut_1080p.png', 'img/red_1080p.png']
confidence_level = 0.91 


while True:
    random_interval = random.uniform(1, 2)
    found = find_and_execute(image_paths, perform_action, start_x, start_y, end_x, end_y, confidence_level)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    print(f"local clear at {current_time}")
    time.sleep(random_interval)
    if found:
        break