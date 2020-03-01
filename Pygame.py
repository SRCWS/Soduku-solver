import pygame
import Full
import sover
import time

pygame.init()

# setting
screenWidth = 1220
screenHeight = 920
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 255)
box_x = 0
box_y = 0
canChange = False
mouse_x = 0
mouse_y = 0
NewGame = False
source = Full.NewGame()
temp = []
mouse_count = 0
start_time = 0
end_time = 0
time_clock = None
new_game = True

for i in source:
    temp.append((i.copy()))


# print(source)
# print(temp)
# source
def newTime():
    global start_time
    global new_game
    start_time = time.time()
    new_game = False


def countTime():
    global end_time
    global time_clock
    end_time = time.time()
    time_count = int(end_time - start_time)
    if len(str(time_count % 60)) == 1:
        ss = "0" + str(time_count % 60)
    else:
        ss = str(time_count % 60)
    if len(str(time_count // 60)) == 1:
        mm = "0" + str(time_count // 60)
    else:
        mm = str(time_count // 60)
    time_clock = (mm + ":" + ss)


def Restart():
    global source
    global temp
    source = []
    temp = []
    source = Full.NewGame()
    for i in source:
        temp.append(i.copy())


# temp.extend(source)
# Restart()
# print(source)
# print(temp)
win = pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
bigFont = pygame.font.Font(pygame.font.get_default_font(), 36)
pygame.display.set_caption("Sudoku")

run = True


def valid(source, number, position):
    # row
    for i in range(len(source[0])):
        if source[position[0]][i] == number and i != position[1]:
            return False
    # columns
    for i in range(len(source[0])):
        if source[i][position[1]] == number and i != position[0]:
            return False
    # box
    box_x = int((position[0] - position[0] % 3) / 3)
    box_y = int((position[1] - position[1] % 3) / 3)
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if source[i][j] == number and (i, j) != position:
                return False

    return True


def backgrade():
    win.fill(white)
    countTime()
    for i in range(3):
        for j in range(3):
            x = 10 + i * 300
            y = 10 + j * 300
            # print(x, y)
            pygame.draw.rect(win, black, (x, y, 300, 300), 4)

    for i in range(9):
        for j in range(9):
            x = 10 + i * 100
            y = 10 + j * 100
            pygame.draw.rect(win, black, (x, y, 100, 100), 2)
    # New Game
    pygame.draw.rect(win, green, (960, 50, 200, 75))
    text_Surface = bigFont.render("New Game", True, black)
    win.blit(text_Surface, dest=(960, 70))
    pygame.draw.rect(win, red, (960, 150, 200, 75))
    text_Surface = bigFont.render("Solver", True, black)
    win.blit(text_Surface, dest=(1000, 170))
    pygame.draw.rect(win, black, (960, 800, 200, 75),4)
    text_Surface = bigFont.render(time_clock,True,black)
    win.blit(text_Surface, dest = (1000,820))

def box():
    for i in range(9):
        for j in range(9):
            x = 50 + i * 100
            y = 50 + j * 100
            if source[i][j] != 0:
                text_Surface = font.render(str(temp[i][j]), True, blue)
                win.blit(text_Surface, dest=(x, y))
            else:
                if temp[i][j] != 0:
                    if valid(temp, temp[i][j], (i, j)):
                        text_Surface = font.render(str(temp[i][j]), True, black)
                    else:
                        text_Surface = font.render(str(temp[i][j]), True, red)
                    win.blit(text_Surface, dest=(x, y))


def on_draw():
    backgrade()
    box()


def click():
    global canChange
    global box_x
    global box_y
    box_x = (mouse_x - 10) // 100
    box_y = (mouse_y - 10) // 100
    # print(box_x, box_y)
    # print(source[box_x][box_y])

    if source[box_x][box_y] == 0:
        # print("A")
        canChange = True
        x = 10 + box_x * 100
        y = 10 + box_y * 100

        pygame.draw.rect(win, green, (x, y, 100, 100))

    else:
        canChange = False


def change(i):
    temp[box_x][box_y] = i


def solver():
    global temp
    temp = []
    for i in source:
        temp.append(i.copy())
    # print(temp)
    sover.solver(temp)
    # print(temp)


# main loop
while run:


    pygame.time.delay(100)
    if new_game:
        newTime()
    backgrade()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if canChange:
        if key[pygame.K_1]:
            change(1)
        if key[pygame.K_2]:
            change(2)
        if key[pygame.K_3]:
            change(3)
        if key[pygame.K_4]:
            change(4)
        if key[pygame.K_5]:
            change(5)
        if key[pygame.K_6]:
            change(6)
        if key[pygame.K_7]:
            change(7)
        if key[pygame.K_8]:
            change(8)
        if key[pygame.K_9]:
            change(9)
        if key[pygame.K_BACKSPACE]:
            change(0)

    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print(mouse_x,mouse_y)
        mouse_count = 1
    if 10 < mouse_x < 910 and 10 < mouse_y < 910:
        click()
    if 960 < mouse_x < 1160 and 50 < mouse_y < 125:
        # print("A")
        if mouse_count == 1:
            Restart()
            newTime()
            mouse_count = 0
    if 960 < mouse_x < 1160 and 170 < mouse_y < 245:
        if mouse_count == 1:
            solver()
            mouse_count = 0

    # print(mouse_x,mouse_y)
    box()
    pygame.display.update()
pygame.quit()
print(temp)
