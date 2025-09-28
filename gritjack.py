import pygame

pygame.init()
screen_width = 1500
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gritjack")

sprite_sheet_image = pygame.image.load('carddeck.png').convert_alpha()

BLACK = (0,0,0)
WHITE = (255, 255, 255)

#sheet is the sprite sheet
#value is what x position the value is on the sheet (0 = 2, 1 = 3, ... 8 = J, 9 = Q, 10 = K, 11 = A)
#suit is what y position the suit is on the sheet (0 = heart, 1 = diamond, 2 = spade, 3 = club, 4 = misc)
#   note: misc has irregular positioning, since it's the non-standard sprites, so it will be more difficult to use
#   see card_test for more details
#width is how wide the sprite is (x)
#height is how tall the sprite is (y)
#scale is the multiplier for the pixel size
def get_image(sheet, value, suit, width, height, scale, color = BLACK):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((value * width), (suit * height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

card = get_image(sprite_sheet_image, 10, 3, 18, 24, 4, BLACK)

#WHEN YOU NEED TO FIND A SPECIFIC CARD/SPRITE, USE THIS FUNCTION TO CALCULATE/FIND WHERE IT IS
def card_test():
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    suits = [0, 1, 2, 3]
    for value in values:
        for suit in suits:
            card = get_image(sprite_sheet_image, value, suit, 18, 24, 4, BLACK)
            screen.blit(card, (100 * value, 100 * suit))
    #back of card
    card = get_image(sprite_sheet_image, 0, 4, 18, 24, 4, BLACK)
    screen.blit(card, (0, 400))
    #right paw
    card = get_image(sprite_sheet_image, 0.8, 2.3333333, 24, 42, 4, BLACK)
    screen.blit(card, (100, 400))
    #left paw
    card = get_image(sprite_sheet_image, 1.8, 2.3333333, 24, 42, 4, BLACK)
    screen.blit(card, (200, 400))
    #>HIT
    card = get_image(sprite_sheet_image, 1.5454, 8.7272, 44, 11, 4, BLACK)
    screen.blit(card, (300, 400))
    #HIT
    card = get_image(sprite_sheet_image, 1.5454, 9.7272, 44, 11, 4, BLACK)
    screen.blit(card, (300, 450))
    #>STAY
    card = get_image(sprite_sheet_image, 2.5682, 8.7272, 44, 11, 4, BLACK)
    screen.blit(card, (500, 400))
    #STAY
    card = get_image(sprite_sheet_image, 2.5682, 9.7272, 44, 11, 4, BLACK)
    screen.blit(card, (500, 450))

hit = get_image(sprite_sheet_image, 1.5454, 9.7272, 44, 11, 4, BLACK)
stay = get_image(sprite_sheet_image, 2.5682, 9.7272, 44, 11, 4, BLACK)
rect = get_image(sprite_sheet_image, 5, 10, 44, 11, 4, BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([176, 44])
        self.image = get_image(sprite_sheet_image, 1.5454, 8.7272, 44, 11, 4, BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500

    def update(self):
        # Define how the sprite updates its state (e.g., movement)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            #self.rect.x -= 1
            if self.rect.x == 500:
                self.image = get_image(sprite_sheet_image, 1.5454, 8.7272, 44, 11, 4, BLACK)
                self.rect.x = 300
        if keys[pygame.K_RIGHT]:
            #self.rect.x += 1
            if self.rect.x == 300:
                self.image = get_image(sprite_sheet_image, 2.5682, 8.7272, 44, 11, 4, BLACK)
                self.rect.x = 500
        if keys[pygame.K_RETURN]:
            if self.rect.x == 300:
                #self.image = get_image(sprite_sheet_image, 1.5454, 9.7272, 44, 11, 4, BLACK)
                self.image = rect
                hit.fill(BLACK)
                stay.fill(BLACK)
            if self.rect.x == 500:
                #self.image = get_image(sprite_sheet_image, 2.5682, 9.7272, 44, 11, 4, BLACK)
                self.image = rect
                hit.fill(BLACK)
                stay.fill(BLACK)
        if keys[pygame.K_RSHIFT]:
            self.image = get_image(sprite_sheet_image, 2.5682, 8.7272, 44, 11, 4, BLACK)
            self.rect.x = 500
            self.rect.y = 500


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()  # Update all sprites
    screen.fill((0, 50, 0))  # Fill background with green
    all_sprites.draw(screen)  # Draw all sprites
    card_test()
    screen.blit(sprite_sheet_image, (0, 600))
    screen.blit(hit, (300, 500))
    screen.blit(stay, (500, 500))
    pygame.display.flip()

pygame.quit()
