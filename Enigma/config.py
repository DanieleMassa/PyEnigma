import pygame
import pyperclip

pygame.init()

# Impostazione della finestra
screen_width = 500
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enigma configuration")

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
