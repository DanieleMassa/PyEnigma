import pygame
import pyperclip
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw


class main_config:
    pygame.init()

    # Impostazione della finestra
    screen_width = 500
    screen_height = 450
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Enigma configurator")

    # Impostazione del font
    font = pygame.font.Font(None, 30)

    # Impostazione dei colori
    bg_color = (51, 51, 51)
    text_color = (242, 228, 206)
    answer_offset = 25

    # Sfondo
    sfondo = pygame.image.load("img/enigma_background.png").convert()

    # Impostazione delle domande
    questions = [
        "Inserire la chiave:",
        "Inserire il 1 anello:",
        "Inserire il 2 anello:",
        "Inserire il 3 anello:",
        "Inserire il 1 collegamento:",
        "Inserire il 2 collegamento:",
        "Inserire il 3 collegamento:"
    ]

    # Impostazione delle risposte
    answers = ["", "", "", "", "", "", ""]

    # Impostazione della variabile che tiene traccia della domanda corrente
    current_question_index = 0
    current_question = questions[current_question_index]
    current_answer = ""

    # Ciclo del gioco
    running = True
    while running:
        # Gestione degli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # Salvataggio della risposta nella variabile corretta
                    answers[current_question_index] = current_answer
                    current_question_index += 1
                    if current_question_index >= len(questions):
                        running = False
                    else:
                        current_question = questions[current_question_index]
                        current_answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Rimozione dell'ultimo carattere dalla risposta corrente
                    current_answer = current_answer[:-1]
                elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    # Incolla il testo dalla clipboard nella risposta corrente
                    current_answer += pyperclip.paste()
                else:
                    # Aggiunta del carattere alla risposta corrente
                    current_answer += event.unicode

        # Impostazione del colore di sfondo e dell'immagine
        screen.fill(bg_color)
        screen.blit(sfondo, (0, 0))

        # Disegno delle domande e delle risposte
        for i, question in enumerate(questions):
            question_surface = font.render(question, True, text_color)
            screen.blit(question_surface, (20, 20 + i * 50))

            if i == current_question_index:
                answer_color = text_color
            else:
                answer_color = (128, 128, 128)  # colore del testo dopo aver premuto invio

            answer_surface = font.render(answers[i], True, answer_color)
            screen.blit(answer_surface, (300 + answer_offset, 20 + i * 50))  # risposta scritta dopo aver premuto invio

        # Scrivi la risposta corrente sulla schermata
        current_answer_surface = font.render(current_answer, True, text_color)
        screen.blit(current_answer_surface, (300 + answer_offset, 20 + current_question_index * 50))
        #                                                                                           ^ risp scrit in tmp real

        # Aggiornamento della schermata
        pygame.display.update()

    # Stampa delle risposte
    print("Chiave:", answers[0].upper())
    print("Primo anello:", answers[1])
    print("Secondo anello:", answers[2])
    print("Terzo anello:", answers[3])
    print("Primo collegamento:", answers[4].upper())
    print("Secondo collegamento:", answers[5].upper())
    print("Terzo collegamento:", answers[6].upper())

    # Uscita dal gioco
    pygame.quit()


class main:

    inp_chiave = main_config.answers[0].upper()
    inp_r1 = main_config.answers[1]
    inp_r2 = main_config.answers[2]
    inp_r3 = main_config.answers[3]
    inp_c1 = main_config.answers[4].upper()
    inp_c2 = main_config.answers[5].upper()
    inp_c3 = main_config.answers[6].upper()

    INPUT_KEY = inp_chiave
    INPUT_R1 = inp_r1
    INPUT_R2 = inp_r2
    INPUT_R3 = inp_r3

    INPUT_C1 = inp_c1
    INPUT_C2 = inp_c2
    INPUT_C3 = inp_c3

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Enigma Machine")

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

    I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")  # Rotore 1 con configurazione originale
    II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")  # Rotore 2 con configurazione originale
    III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")  # Rotore 3 con configurazione originale
    IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")  # Rotore 4 con configurazione originale
    V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")  # Rotore 5 con configurazione originale

    A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
    B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
    KB = Keyboard()
    # PB = Plugboard(["CD", "AG", "OR"])
    PB = Plugboard([INPUT_C1, INPUT_C2, INPUT_C3])

    ENIGMA = Enigma(A, I, II, III, PB, KB)

    ENIGMA.set_rings((int(INPUT_R1), int(INPUT_R2), int(INPUT_R3)))

    ENIGMA.set_key(INPUT_KEY)

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
                    INPUT += " "
                    OUTPUT += " "
                else:
                    key = event.unicode
                    if key in ALPHABET_LOWERCASE or key in ALPHABET_UPPERCASE:
                        letter = key.upper()
                        INPUT = INPUT + letter
                        PATH, cipher = ENIGMA.encipher(letter)
                        print(PATH)
                        OUTPUT = OUTPUT + cipher
