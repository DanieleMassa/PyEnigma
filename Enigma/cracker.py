import os

image_path = os.path.join("img", "Enigma_Logo.png")

if not os.path.exists(image_path):
    print("File dell'immagine non trovato!")
else:
    print("File dell'immagine trovato correttamente.")
