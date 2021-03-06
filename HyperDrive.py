
import pygame
import random 
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 480
HEIGHT = 600
FPS = 60 #Frames per Second
POWERUP_TIME = 5000

#define colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init() #Handles sound effects
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Galaga")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def newSquad():
    a = Enemy()
    all_sprites.add(a)
    aliens.add(a)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (80, 48))
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius )
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -10 
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    
    def update(self):
        #timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        #UNHIDE IF HIDDEN
        if self.hidden and pygame.time.get_ticks() - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        
        
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9.5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 9.5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        # Keep sprite on screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        #hide the player temporarily
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(alien_images),(100,60))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200,-40)
        self.speedy = random.randrange(1, 13)
        self.speedx = random.randrange(-3, 3)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(1, 10)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius )
        self.rect.y = random.randrange(-200,-40)
        self.speedy = random.randrange(1, 9)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0 #Rotation
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()


    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield','gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5
    
    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 25

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, 'GALAGA V3.0', 64, WIDTH / 2, HEIGHT /4)
    draw_text(screen, 'Use the Arrow keys to move and Space Bar to fire', 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Press any key to begin', 18, WIDTH /2, HEIGHT * 3 /4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

#Load all game graphics
background = pygame.image.load(path.join(img_dir, 'Background-4.jpg')).convert()
background_rect = background.get_rect()
x = 0
y = 0

x1 = 0
y1 = -HEIGHT

alien_images = []
alien_list = ['Alien-Scout.png','Alien-Destroyer.png','Alien-Frigate.png']
for img in alien_list:
    alien_images.append(pygame.image.load(path.join(img_dir, img)).convert())


player_img = pygame.image.load(path.join(img_dir, 'player_ship.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25,19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
meteor_images = []

meteor_list = ['meteorBrown_big1.png','meteorBrown_big2.png','meteorBrown_big3.png',
                'meteorBrown_big4.png','meteorBrown_med1.png','meteorBrown_med3.png',
                'meteorBrown_small1.png','meteorBrown_small2.png','meteorBrown_tiny1.png',
                'meteorBrown_tiny2.png','meteorGrey_big1.png','meteorGrey_big2.png',
                'meteorGrey_big3.png','meteorGrey_big4.png','meteorGrey_med1.png',
                'meteorGrey_med2.png','meteorGrey_small1.png','meteorGrey_small2.png',
                'meteorGrey_tiny1.png','meteorGrey_tiny2.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(24):
    filename = 'expl_01_{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32 ,32))
    explosion_anim['sm'].append(img_sm)
    #player explosion images same 24
    filename = 'expl_10_00{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir,'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir,'bolt_gold.png')).convert()


#Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir,'Laser1.wav'))
shield_sound = pygame.mixer.Sound(path.join(snd_dir,'shieldPowerup.wav'))
power_sound = pygame.mixer.Sound(path.join(snd_dir,'gunPowerup.wav'))
explosion = pygame.mixer.Sound(path.join(snd_dir, 'Explosion2.wav'))
player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'playerExplosion.wav')) 
shoot_sound.set_volume(0.5)
pygame.mixer.music.load(path.join(snd_dir, 'Orbital Colossus.mp3'))
# pygame.mixer.music.set_volume(0.6) 
pygame.mixer.music.play(loops = -1) 

# Game Loop
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        #Sprite Groups
        
        
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        aliens = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        for i in range(3):
            newSquad()
        for i in range(8):
            newmob()
        all_sprites.add(bullets)
        all_sprites.add(player)


        score  = 0 
    # keep loop running at the right speed
    clock.tick(FPS)
    
    #Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    
    #Update
    all_sprites.update()

    # CHECK TO SEE IF A BULLET HIT A MOB
    mob_hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in mob_hits:
        score += 50 - hit.radius
        explosion.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    alien_hits = pygame.sprite.groupcollide(aliens,bullets,True,True)
    for hit in alien_hits:
        score += 100 - hit.radius
        explosion.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newSquad()



    # check to see if a mob hit the player
    player_hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle) #If not collide argument then rectangle is default
    for hit in player_hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    #Check to see if an alien hit the player
    alien_hits = pygame.sprite.spritecollide(player,aliens,True, pygame.sprite.collide_circle)
    for hit in alien_hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newSquad()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    #check to see if player hit a powerup
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            shield_sound.play()
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()
            power_sound.play()


    #If the player died and the explosion has finished playing 
    if player.lives == 0 and not death_explosion.alive():
        game_over = True

    #Draw / render
    screen.blit(background, background_rect)
    y1 += 10
    y += 10
    screen.blit(background, (x,y))
    screen.blit(background, (x1,y1))
    if y > HEIGHT:
        y =- HEIGHT
    if y1 > HEIGHT:
        y1 =- HEIGHT
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
