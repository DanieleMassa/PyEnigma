import pygame


class Keyboard:

    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

    def draw(self, screen, x, y, w, h, font):
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)
        
        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/2, y+(i+1)*h/27))
            screen.blit(letter, text_box)
