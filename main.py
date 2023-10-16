import pyautogui, sys, random, time



def find_and_execute(image_paths, action_function, start_x, start_y, end_x, end_y, confidence):
    search_region = (start_x, start_y, end_x - start_x, end_y - start_y)
    for image_path in image_paths:
        position = pyautogui.locateOnScreen(image_path, region=search_region, confidence=confidence)

        if position is not None:
            action_function()
            return True
    return False

# Beispielaufruf der Funktion
# Ersetzen Sie 'YOUR_IMAGE_PATH_1' und 'YOUR_IMAGE_PATH_2' durch die Pfade zu Ihren Bildern und definieren Sie Ihre eigene Funktionslogik.
# Definieren Sie die Start- und Endpunkte der Suchregion entsprechend Ihrer Anforderungen.

def perform_action():
    # Hier können Sie Ihre eigene Funktionslogik einfügen, die ausgeführt wird, wenn eines der Bilder gefunden wird.
    print("warping to safespot")
    sys.exit()

start_x, start_y = 387, 464  # Beispiel Startpunkt der Suchregion
end_x, end_y = 562, 907  # Beispiel Endpunkt der Suchregion
#image_paths = ['img/neut_4k.png', 'img/red_4k.png']  # Beispiel Pfade zu den Bildern
image_paths = ['img/neut_1080p.png', 'img/red_1080p.png']
confidence_level = 0.91  # Beispielwert für die Intensität der Bilderkennung


while True:
    
    random_intervall = random.uniform(1, 2)

    found = find_and_execute(image_paths, perform_action, start_x, start_y, end_x, end_y, confidence_level)
    time.sleep(random_intervall)
    print("local clear!", random_intervall)
    if found:
        perform_action()
        break