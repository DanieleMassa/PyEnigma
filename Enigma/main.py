import pygame
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

"""
INPUT_MACHINE = input("Inserire la versione della macchina: ")
if INPUT_MACHINE == "Versioni macchine":
    print("A: EJMZALYXVBWFCRQUONTSPIKHGD")
    print("B: YRUHQSLDPXNGOKMIEBFZCWVJAT")
    print("C: FVPJIAOYEDRZXWGCTKUQSBNMHL")
    input("Inserire la versione della macchina: ")
elif INPUT_MACHINE == int(2) or int(1) or int(3):
    

else:
    pass
"""

INPUT_KEY = input("Inserire la chiave: ")
INPUT_R1 = input("Inserire il primo anello: ")
INPUT_R2 = input("Inserire il secondo anello: ")
INPUT_R3 = input("Inserire il terzo anello: ")

INPUT_C1 = input("Inserire il primo collegamento: ")
INPUT_C2 = input("Inserire il secondo collegamento: ")
INPUT_C3 = input("Inserire il terzo collegamento: ")


pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma")

MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top": 200, "bottom": 200, "left": 100, "right": 100}
GAP = 100
INPUT = ""
OUTPUT = ""
PATH = []


I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()
# PB = Plugboard(["CD", "AG", "OR"])
PB = Plugboard([INPUT_C1, INPUT_C2, INPUT_C3])

ENIGMA = Enigma(A, I, II, III, PB, KB)

ENIGMA.set_rings((int(INPUT_R1), int(INPUT_R2), int(INPUT_R3)))

ENIGMA.set_key(INPUT_KEY)
"""
message = "DANIELE"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)

I.show()
I.rotate_to_letter("G")
I.show()
"""

animating = True
while animating:
    SCREEN.fill("#333333")

    # txt input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3))
    SCREEN.blit(text, text_box)
    # txt output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3 + 35))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in ALPHABET_LOWERCASE or key in ALPHABET_UPPERCASE:
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT = OUTPUT + cipher
