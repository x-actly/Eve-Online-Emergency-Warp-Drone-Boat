import pyautogui
import sys

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
    print("Bild gefunden, Aktion wird ausgeführt.")
    sys.exit()

start_x, start_y = 374, 605  # Beispiel Startpunkt der Suchregion
end_x, end_y = 497, 1323  # Beispiel Endpunkt der Suchregion
#image_paths = ['img/neut_4k.png', 'img/red_4k.png']  # Beispiel Pfade zu den Bildern
image_paths = ['img/neut_1080p.png', 'img/red_1080p.png']
confidence_level = 0.88  # Beispielwert für die Intensität der Bilderkennung

while True:
    found = find_and_execute(image_paths, perform_action, start_x, start_y, end_x, end_y, confidence_level)
    print("Bilder werden gesucht!")
    if found:
        perform_action()
        break