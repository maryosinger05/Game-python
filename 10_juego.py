import pygame, os, random
import pygame.locals



class Backgroud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","2 Locations","Backgrounds", "1.png")).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","2 Locations","Tiles", "Tile_07.png")).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","2 Locations","Tiles", "Tile_123.png")).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

class UnderFloor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","2 Locations","Tiles", "Tile_09.png")).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets","1 Main Characters","3", "stay1.png")).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

    
        
pygame.init()

all_sprites = pygame.sprite.Group()

platform_rects = []

screen = pygame.display.set_mode([500,400])
clock = pygame.time.Clock()

done = False

white = (255,255,255)

#--------------Background------------------
backgroud = Backgroud()
backgroud.rect.x = 0
backgroud.rect.y = 0
all_sprites.add(backgroud)
#--------------Background------------------

#--------------Floor------------------
for i in range(0,500,15):
    
    tile_06 = Floor()
    tile_06.rect.x = i
    tile_06.rect.y = 340
    tile_06_list = pygame.sprite.Group()
    platform_rects.append(tile_06.rect)
    tile_06_list.add(tile_06)
    all_sprites.add(tile_06)

#--------------UnderFloor------------------
for i in range(0,500,15):
    for j in range(355,400,8):
        tile_09 = UnderFloor()
        tile_09.rect.x = i
        tile_09.rect.y = j
        tile_09_list = pygame.sprite.Group()
        tile_09_list.add(tile_09)
        all_sprites.add(tile_09)

#--------------Platforms------------------
for i in range(30):
    tile_123 = Platform()
    tile_123.rect.x = random.randrange(0,500)
    tile_123.rect.y = random.randrange(0,340)
    tile_123_list = pygame.sprite.Group()
    platform_rects.append(tile_123.rect)
    tile_123_list.add(tile_123)
    all_sprites.add(tile_123)




"""for i in range(30):
    tile_123 = Platform()
    tile_123.rect.x = random.randrange(0,500)
    tile_123.rect.y = random.randrange(0,340)
    tile_123_list = pygame.sprite.Group()
    tile_123_list.add(tile_123)
    all_sprites.add(tile_123)"""

#--------------Player------------------
player = Player()
player.rect.x = 200
player.rect.y = 100
player.rect.height = 34
player.rect.width = 32
gravity = 2.1
jump = 200
player_speed_y = 0
player_speed_x = 0
all_sprites.add(player)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
        


        if player.rect.y < 320 or player.rect.y > 190:
            if pygame.KEYDOWN and pygame.KEYUP:
                pygame.key.set_repeat()
                


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_speed_y = -4
                pygame.key.set_repeat()
            if event.key == pygame.K_RIGHT:
                player_speed_x = 4
            if event.key == pygame.K_LEFT:
                player_speed_x = -4
        


        if event.type == pygame.KEYUP:
            """if event.key == pygame.K_SPACE:
                player_speed_y = -4
                pygame.key.set_repeat()"""
            if event.key == pygame.K_RIGHT:
                player_speed_x = 0
            if event.key == pygame.K_LEFT:
                player_speed_x = 0



    player.rect.y += player_speed_y
    player.rect.x += player_speed_x


    
    

    

    for platform_rect in platform_rects:
            if platform_rect.y + player.rect.height < player.rect.y:
                
                continue
            #print(platform)
            if player.rect.colliderect(platform_rect):
                player.rect.y = platform_rect.y - player.rect.height
                player_speed_y = 0
                print("colision detectada")
            else:
                player.rect.y += gravity

    if player.rect.y < jump:
        player_speed_y *= -1




    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    
    #print(mouse_pos)

    screen.fill(white)
    all_sprites.draw(screen)
    
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()