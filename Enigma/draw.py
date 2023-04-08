import pygame


def draw(enigma, path, screen, width, height, margins, gap, font):

    # width and height of coordinates
    w = (width - margins["left"] - margins["right"] - 5*gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # path coordinates
    y = [margins["top"] + (signal + 1) * h / 27 for signal in path]
    x = [width - margins["right"] - w/2]
    for i in [4, 3, 2, 1, 0]:
        x.append(margins["left"] + i * (w + gap) + w * 3 / 4)
        x.append(margins["left"] + i * (w + gap) + w * 1 / 4)
    x.append(margins["left"] + w * 3 / 4)
    for i in [1, 2, 3, 4]:
        x.append(margins["left"] + i * (w + gap) + w * 1 / 4)
        x.append(margins["left"] + i * (w + gap) + w * 3 / 4)
    x.append(width - margins["right"] - w / 2)
    # draw path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i - 1], y[i - 1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # coordinates
    x = margins["left"]
    y = margins["top"]

    # draw enigma components
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # draw names
    names = ["Riflettore", "Sinistro", "Centrale", "Destro", "PlugBoard", "Input/Output"]
    y = margins["top"] * 0.8
    for i in range(6):
        x = margins["left"] + w / 2 + i * (w + gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center=(x, y))
        screen.blit(title, text_box)
