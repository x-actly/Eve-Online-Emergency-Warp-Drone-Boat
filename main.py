import pyautogui, sys, random, time, pygame, time, threading
from datetime import datetime
from functions import emergency_warp
from functions import targeting

alarm_played = False

additional_thread_running = True

# Detection Area
start_x, start_y = 357, 343  
end_x, end_y = 487, 948

# safespot
safe_x, safe_y = 1700, 1068

# targeting
targeting_x, targeting_y = 2048, 804

# Image Path
image_paths = ['img/neut_4k.png', 'img/red_4k.png', 'img/-5_1440p.png', 'img/-10_1440p.png', 
               'img/neut_1080p.png', 'img/red_1080p.png', 'img/-5_1080p.png', 'img/-5_1440p.png', 
               'img/-10_1080p.png', 'img/-10_1440p.png']  
#image_paths = ['img/neut_1080p.png', 'img/red_1080p.png', 'img/-5.png', 'img/-10.png']

# Confidence Lvl - Laptop = 0.84 at 1080p, PC = 0.85 at 1440p
confidence_level = 0.85 

def find_and_execute(image_paths, action_function, start_x, start_y, end_x, end_y, confidence):
    search_region = (start_x, start_y, end_x - start_x, end_y - start_y)
    for image_path in image_paths:
        position = pyautogui.locateOnScreen(image_path, region=search_region, confidence=confidence)

        if position is not None:
            action_function()
            return True
    return False

def additional_thread_function():
    random_interval = random.uniform(60, 70)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    global additional_thread_running
    while additional_thread_running:
        
        time.sleep(random_interval)
        print(f"{current_time} - targeting")
        targeting(targeting_x, targeting_y)



additional_thread = threading.Thread(target=additional_thread_function)
additional_thread.daemon = True 
additional_thread.start()

def perform_action():
    global alarm_played
    if not alarm_played:
        pygame.mixer.init()
        pygame.mixer.music.load('sound/alarm.mp3')
        pygame.mixer.music.play()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{current_time} - emergency warp")
        while pygame.mixer.music.get_busy():
            continue
        alarm_played = True
        emergency_warp(safe_x, safe_y)

    sys.exit()

while True:
    random_interval = random.uniform(1, 2)
    found = find_and_execute(image_paths, perform_action, start_x, start_y, end_x, end_y, confidence_level)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    print(f"{current_time} - local clear")
    time.sleep(random_interval)
    if found:
        additional_thread_running = False
        break