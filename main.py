import pyautogui, sys, random, time, pygame, time, threading
from datetime import datetime
from functions import emergency_warp
from functions import targeting
import tkinter as tk

alarm_played = False

additional_thread_running = True

# Detection Area
start_x, start_y = 150, 652 
end_x, end_y = 354, 988

# safespot
safe_x, safe_y = 1096, 271
safe_window_size = 6  # Fenstergröße um den Mittelpunkt in jede Richtung

# Koordinaten des Targeting-Bereichs
targeting_x, targeting_y = 1054, 666
targeting_window_size = 6  # Fenstergröße um den Mittelpunkt in jede Richtung

# Funktion zum Schließen der Fenster
def close_windows(event=None):
    root.destroy()
    safe_root.destroy()
    targeting_root.destroy()

# Tkinter-Fenster einrichten
root = tk.Tk()
root.overrideredirect(True)  # Entfernt die Fensterrahmen und die Titelleiste
root.attributes("-alpha", 0.1)  # Setzen Sie die Transparenz des Fensters (0 ist vollständig transparent, 1 ist undurchsichtig)

# Die Größe des Tkinter-Fensters basierend auf den Koordinaten des Rahmens festlegen
window_width = end_x - start_x
window_height = end_y - start_y
root.geometry(f"{window_width}x{window_height}+{start_x}+{start_y}")

# Ein Canvas hinzufügen
canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0)
canvas.pack()

# Funktion zum Zeichnen des Rahmens
def draw_rectangle(start_x, start_y, end_x, end_y):
    canvas.create_rectangle(0, 0, end_x - start_x, end_y - start_y, outline="red", width=3, fill="red")

# Den Rahmen zeichnen
draw_rectangle(start_x, start_y, end_x, end_y)

# Tkinter-Fenster für den Safespot einrichten
safe_root = tk.Tk()
safe_root.overrideredirect(True)  # Entfernt die Fensterrahmen und die Titelleiste
safe_root.attributes("-alpha", 0.5)  # Setzen Sie die Transparenz des Fensters (0 ist vollständig transparent, 1 ist undurchsichtig)

# Die Größe des Tkinter-Fensters für den Safespot festlegen
safe_root.geometry(f"{safe_window_size}x{safe_window_size}+{safe_x-safe_window_size//2}+{safe_y-safe_window_size//2}")

# Ein Canvas für den Safespot hinzufügen
safe_canvas = tk.Canvas(safe_root, width=safe_window_size, height=safe_window_size, highlightthickness=0)
safe_canvas.pack()

# Funktion zum Zeichnen des Safespot-Rahmens
def draw_safe_rectangle():
    safe_canvas.create_rectangle(0, 0, safe_window_size, safe_window_size, outline="red", width=3, fill="red")

# Den Safespot-Rahmen zeichnen
draw_safe_rectangle()

# Tkinter-Fenster für den Targeting-Bereich einrichten
targeting_root = tk.Tk()
targeting_root.overrideredirect(True)  # Entfernt die Fensterrahmen und die Titelleiste
targeting_root.attributes("-alpha", 0.5)  # Setzen Sie die Transparenz des Fensters (0 ist vollständig transparent, 1 ist undurchsichtig)

# Die Größe des Tkinter-Fensters für den Targeting-Bereich festlegen
targeting_root.geometry(f"{targeting_window_size}x{targeting_window_size}+{targeting_x-targeting_window_size//2}+{targeting_y-targeting_window_size//2}")

# Ein Canvas für den Targeting-Bereich hinzufügen
targeting_canvas = tk.Canvas(targeting_root, width=targeting_window_size, height=targeting_window_size, highlightthickness=0)
targeting_canvas.pack()

# Funktion zum Zeichnen des Targeting-Rahmens
def draw_targeting_rectangle():
    targeting_canvas.create_rectangle(0, 0, targeting_window_size, targeting_window_size, outline="red", width=3, fill="red")

# Den Targeting-Rahmen zeichnen
draw_targeting_rectangle()

# Tastendruck zum Schließen der Fenster binden
root.bind("<Key>", close_windows)
safe_root.bind("<Key>", close_windows)
targeting_root.bind("<Key>", close_windows)

root.mainloop()

# Image Path
image_paths = ['img/neut_4k.png', 'img/red_4k.png', 'img/-5_1440p.png', 'img/-10_1440p.png', 
               'img/neut_1080p.png', 'img/red_1080p.png', 'img/-5_1080p.png', 'img/-5_1440p.png', 
               'img/-10_1080p.png', 'img/-10_1440p.png', 'img/neut_1080p_red.png']  
#image_paths = ['img/neut_1080p.png', 'img/red_1080p.png', 'img/-5.png', 'img/-10.png']

# Confidence Lvl - Laptop = 0.84 at 1080p, PC = 0.85 at 1440p
confidence_level = 0.84 

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
        #targeting(targeting_x, targeting_y)



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
    try:
        random_interval = random.uniform(1, 2)
        found = find_and_execute(image_paths, perform_action, start_x, start_y, end_x, end_y, confidence_level)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        print(f"{current_time} - local clear")
        time.sleep(random_interval)
        if found:
            additional_thread_running = False
            break
    except KeyboardInterrupt:
        print("Keyboard interruption detected. Exiting the program.")
        additional_thread_running = False
        break