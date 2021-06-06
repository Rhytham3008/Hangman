import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("The last game")

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx = GAP*2 + ((RADIUS*2 + GAP)*(i%13))
    y = starty +((GAP +RADIUS*2)*(i // 13))
    letters.append([x,y,chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

images = []
for i in range(7):
    image = pygame.image.load('hangman' + str(i)+'.png')
    images.append(image)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

hangman_index = 0
words = ["WINDOWS", "MAC", "LINUX", "POPOS", "GOOGLE", "AMAZON"]
word = random.choice(words)
guessed = []

clock = pygame.time.Clock()
play = True

def draw():
    win.fill(white)

    text = TITLE_FONT.render("HANGMAN!", 1, black)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    display_word = ""
    for ltr in word:
        if ltr in guessed:
            display_word += ltr + " "
        else:
            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, black)
    win.blit(text, (400, 200))

    for ltr in letters:
        x, y, ltr, visible = ltr
        if visible:
            pygame.draw.circle(win, black, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))


    win.blit(images[hangman_index], (150,100))
    pygame.display.update()

while play:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - mx)**2 + (y - my)**2)
                    if dis< RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_index += 1
    draw()
    victory = True
    for letter in word:
        if letter not in guessed:
            victory = False
            break

    if victory:
        pygame.time.delay(1500)
        win.fill(white)
        text = WORD_FONT.render("You Won!", 1, green)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break

    if hangman_index == 6:
        pygame.time.delay(1500)
        win.fill(white)
        text = WORD_FONT.render("You Lost!", 1, green)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break

pygame.quit()