import pygame, random

#Initialize pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon")

#Create images. Returns a surface object with the image drawn on it
#We can then get the rect of the surface and use the rect to position the image
dragon_image = pygame.image.load("dragon.png")
dragon_rect = dragon_image.get_rect()
#dragon_rect.topleft = (0, 0)
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.topleft = (0, 0)

#Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 120, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(CYAN)

#see all available system fonts
# fonts = pygame.font.get_fonts()

#Define fonts
# system_font = pygame.font.SysFont("calibri", 64)
# custom_font = pygame.font.Font("SunnyspellsRegular.otf", 32)

#Define text
# system_text = system_font.render("Dragon rules!", True, BLUE, YELLOW)
# system_text_rect = system_text.get_rect()
# system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
#
# custom_text = custom_font.render("Move the dragon soon!", True, DARK_GREEN)
# custom_text_rect  =custom_text.get_rect()
# custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#Load sound effects
# noise_sound = pygame.mixer.Sound("noise_sound.wav")
# jingle_sound = pygame.mixer.Sound("jingle_sound.wav")

#Play the sound effect
# noise_sound.play()
# pygame.time.delay(2000)
# jingle_sound.play()
# pygame.time.delay(2000)

#Load background music
#pygame.mixer.music.load("Blanilla_Triple_Seq.wav")

#Play and stop the music
#pygame.mixer.music.play(-1, 0.0) # -1 means you play it infinitely (or you can do 1 if you want to play it only once) and 0.0 means you start at the begining

#Change the volume of a sound effect
# jingle_sound.set_volume(.1)

#Set FPS (frames per second) and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 20


#Draw various shapes on display
#Line(surface, color, start point, end point, thickness)
#pygame.draw.line(display_surface, MAGENTA, (0, 0), (100, 100), 5)

#Circle(surface, color, center, radius, thickness....0 for fill)
#pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)

#Rectangle(surface, color, (top-left x, top-left y, width, height), thickness)
#pygame.draw.rect(display_surface, GREEN, (400, 100, 400, 100), 2)

#The main game loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        #Check for discrete movement
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         dragon_rect.x -= VELOCITY
        #     if event.key == pygame.K_RIGHT:
        #         dragon_rect.x += VELOCITY
        #     if event.key == pygame.K_UP:
        #         dragon_rect.y -= VELOCITY
        #     if event.key == pygame.K_DOWN:
        #         dragon_rect.y += VELOCITY

        #Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

        #Check for mouse movement
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     dragon_rect.centerx = mouse_x
        #     dragon_rect.centery = mouse_y

        #Drag the object when the mouse button is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    #Get list of keys currently being held down
    keys = pygame.key.get_pressed()

    #Move the dragon continuously
    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    #Check for collision of the two rects
    if dragon_rect.colliderect(coin_rect):
        coin_rect.left = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.top = random.randint(0, WINDOW_HEIGHT - 32)


    #Fill the display surface to cover all images
    display_surface.fill(CYAN)

    #Draw rectangles to represent the rect's of each object
    # pygame.draw.rect(display_surface, RED, dragon_rect, 1)
    # pygame.draw.rect(display_surface, YELLOW, coin_rect, 1)

    #blit (copy) the text surfaces to the display surface
    #display_surface.blit(system_text, system_text_rect)
    #display_surface.blit(custom_text, custom_text_rect)

    #blit(copy) a surface object at the given coordinates t our display
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    #update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()

