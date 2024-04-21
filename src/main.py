from src.bullet import *
from src.cell import *
from src.enemy import *
from src.enemyBullet import *
from src.player import *
from src.virus import *

IMAGES_PATH = "./images/"
SOUNDS_PATH = "./sounds/"

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.sw = 1000
        self.sh = 600

        # Images settings
        self.background = pygame.image.load("./images/background.png")
        self.playerShip = pygame.image.load("./images/ship.png")
        self.alienShip = pygame.image.load("./images/virus2.png")
        self.cell = pygame.image.load("./images/cell.png")
        self.asteroid50 = pygame.image.load("./images/virus1.png")
        self.asteroid100 = pygame.image.load("./images/dust2.png")
        self.asteroid150 = pygame.image.load("./images/dust1.png")
        self.asteroids_pics = [self.asteroid50, self.asteroid100, self.asteroid150]

        # Sounds settings
        pygame.mixer.init()
        self.shoot = pygame.mixer.Sound("./sounds/shoot.wav")
        self.bangLargeSound = pygame.mixer.Sound("./sounds/bangLarge.wav")
        self.bangSmallSound = pygame.mixer.Sound("./sounds/bangSmall.wav")
        self.backgroundSound = pygame.mixer.Sound("./sounds/background.wav")
        self.shoot.set_volume(0.25)
        self.bangLargeSound.set_volume(0.25)
        self.bangSmallSound.set_volume(0.25)
        self.backgroundSound.set_volume(0.20)

        # Set window caption and create window
        pygame.display.set_caption("Asteroids")
        self.win = pygame.display.set_mode((self.sw, self.sh))
        self.clock = pygame.time.Clock()

        # Game variables
        self.gameover = False
        self.lives = 3
        self.score = 0
        self.rapidFire = False
        self.rfStart = -1
        self.isSoundOn = True
        self.highScore = 0

        # Initialize game objects
        self.player = Player(self.sw, self.sh, self.playerShip)
        self.playerBullets = []
        self.asteroids = []
        self.count = 0
        self.stars = []
        self.aliens = []
        self.alienBullets = []

        # Start background music
        self.backgroundSound.play()

    def redrawGameWindow(self):
        """Draw game window."""
        self.win.blit(self.background, (0, 0))
        font = pygame.font.SysFont("arial", 40)
        livesText = font.render("Lives: " + str(self.lives), 1, (0, 0, 0))
        playAgainText = font.render("Press Tab to Play Again", 1, (255, 255, 255))
        scoreText = font.render("Score: " + str(self.score), 1, (0, 0, 0))
        highScoreText = font.render("High Score: " + str(self.highScore), 1, (0, 0, 0))

        self.player.draw(self.win)
        for asteroid in self.asteroids:
            asteroid.draw(self.win)
        for playerBullet in self.playerBullets:
            playerBullet.draw(self.win)
        for star in self.stars:
            star.draw(self.win)
        for alien in self.aliens:
            alien.draw(self.win)
        for alienBullet in self.alienBullets:
            alienBullet.draw(self.win)

        if self.rapidFire:
            pygame.draw.rect(self.win, (0, 0, 0), [self.sw // 2 - 51, 19, 102, 22])
            pygame.draw.rect(
                self.win,
                (255, 255, 255),
                [
                    self.sw // 2 - 50,
                    20,
                    100 - 100 * (self.count - self.rfStart) / 500,
                    20,
                ],
            )

        if self.gameover:
            self.win.blit(
                playAgainText,
                (
                    self.sw // 2 - playAgainText.get_width() // 2,
                    self.sh // 2 - playAgainText.get_height() // 2,
                ),
            )
        self.win.blit(scoreText, (self.sw - scoreText.get_width() - 25, 25))
        self.win.blit(livesText, (25, 25))
        self.win.blit(
            highScoreText,
            (self.sw - highScoreText.get_width() - 25, 35 + scoreText.get_height()),
        )
        pygame.display.update()

    def run(self):
        run = True
        while run:
            self.clock.tick(60)
            self.count += 1
            if not self.gameover:
                # Game logic
                if self.count % 50 == 0:
                    ran = random.choice([1, 1, 1, 2, 2, 3])
                    self.asteroids.append(
                        Virus(self.sw, self.sh, ran, self.asteroids_pics)
                    )
                if self.count % 1000 == 0:
                    self.stars.append(Cell(self.sw, self.sh, self.cell))
                if self.count % 750 == 0:
                    self.aliens.append(Enemy(self.sw, self.sh, self.alienShip))
                for i, a in enumerate(self.aliens):
                    a.x += a.xv
                    a.y += a.yv
                    if (
                        a.x > self.sw + 150
                        or a.x + a.w < -100
                        or a.y > self.sh + 150
                        or a.y + a.h < -100
                    ):
                        self.aliens.pop(i)
                    if self.count % 60 == 0:
                        self.alienBullets.append(
                            EnemyBullet(self.player, a.x + a.w // 2, a.y + a.h // 2)
                        )

                    for b in self.playerBullets:
                        if (a.x <= b.x <= a.x + a.w) or a.x <= b.x + b.w <= a.x + a.w:
                            if (
                                a.y <= b.y <= a.y + a.h
                            ) or a.y <= b.y + b.h <= a.y + a.h:
                                self.aliens.pop(i)
                                if self.isSoundOn:
                                    self.bangLargeSound.play()
                                self.score += 50
                                break

                for i, b in enumerate(self.alienBullets):
                    b.x += b.xv
                    b.y += b.yv
                    if (
                        (
                            self.player.x - self.player.w // 2
                            <= b.x
                            <= self.player.x + self.player.w // 2
                        )
                        or self.player.x - self.player.w // 2
                        <= b.x + b.w
                        <= self.player.x + self.player.w // 2
                    ):
                        if (
                            (
                                self.player.y - self.player.h // 2
                                <= b.y
                                <= self.player.y + self.player.h // 2
                            )
                            or self.player.y - self.player.h // 2
                            <= b.y + b.h
                            <= self.player.y + self.player.h // 2
                        ):
                            self.lives -= 1
                            self.alienBullets.pop(i)
                            break

                self.player.updateLocation()
                for b in self.playerBullets:
                    b.move()
                    if b.checkOffScreen():
                        self.playerBullets.pop(self.playerBullets.index(b))

                for a in self.asteroids:
                    a.x += a.xv
                    a.y += a.yv

                    if (
                        self.player.x - self.player.w // 2
                        <= a.x
                        <= self.player.x + self.player.w // 2
                    ) or (
                        self.player.x + self.player.w // 2
                        >= a.x + a.w
                        >= self.player.x - self.player.w // 2
                    ):
                        if (
                            self.player.y - self.player.h // 2
                            <= a.y
                            <= self.player.y + self.player.h // 2
                        ) or (
                            self.player.y - self.player.h // 2
                            <= a.y + a.h
                            <= self.player.y + self.player.h // 2
                        ):
                            self.lives -= 1
                            self.asteroids.pop(self.asteroids.index(a))
                            if self.isSoundOn:
                                self.bangLargeSound.play()
                            break

                    for b in self.playerBullets:
                        if (a.x <= b.x <= a.x + a.w) or a.x <= b.x + b.w <= a.x + a.w:
                            if (
                                a.y <= b.y <= a.y + a.h
                            ) or a.y <= b.y + b.h <= a.y + a.h:
                                if a.rank == 3:
                                    if self.isSoundOn:
                                        self.bangLargeSound.play()
                                    self.score += 10
                                    na1 = Virus(
                                        self.sw, self.sh, 2, self.asteroids_pics
                                    )
                                    na2 = Virus(
                                        self.sw, self.sh, 2, self.asteroids_pics
                                    )
                                    na1.x = a.x
                                    na2.x = a.x
                                    na1.y = a.y
                                    na2.y = a.y
                                    self.asteroids.append(na1)
                                    self.asteroids.append(na2)
                                elif a.rank == 2:
                                    if self.isSoundOn:
                                        self.bangSmallSound.play()
                                    self.score += 20
                                    na1 = Virus(
                                        self.sw, self.sh, 1, self.asteroids_pics
                                    )
                                    na2 = Virus(
                                        self.sw, self.sh, 1, self.asteroids_pics
                                    )
                                    na1.x = a.x
                                    na2.x = a.x
                                    na1.y = a.y
                                    na2.y = a.y
                                    self.asteroids.append(na1)
                                    self.asteroids.append(na2)
                                else:
                                    self.score += 30
                                    if self.isSoundOn:
                                        self.bangSmallSound.play()
                                self.asteroids.pop(self.asteroids.index(a))
                                self.playerBullets.pop(self.playerBullets.index(b))
                                break

                for s in self.stars:
                    s.x += s.xv
                    s.y += s.yv
                    if (
                        s.x < -100 - s.w
                        or s.x > self.sw + 100
                        or s.y > self.sh + 100
                        or s.y < -100 - s.h
                    ):
                        self.stars.pop(self.stars.index(s))
                        break
                    for b in self.playerBullets:
                        if (s.x <= b.x <= s.x + s.w) or s.x <= b.x + b.w <= s.x + s.w:
                            if (
                                s.y <= b.y <= s.y + s.h
                            ) or s.y <= b.y + b.h <= s.y + s.h:
                                self.rapidFire = True
                                self.rfStart = self.count
                                self.stars.pop(self.stars.index(s))
                                self.playerBullets.pop(self.playerBullets.index(b))
                                break

                if self.lives <= 0:
                    self.gameover = True

                if self.rfStart != -1:
                    if self.count - self.rfStart > 500:
                        self.rapidFire = False
                        self.rfStart = -1

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.player.turn("left")
                if keys[pygame.K_RIGHT]:
                    self.player.turn("right")
                if keys[pygame.K_UP]:
                    self.player.move("forward")
                if keys[pygame.K_DOWN]:
                    self.player.move("backward")
                if keys[pygame.K_SPACE]:
                    if self.rapidFire:
                        self.playerBullets.append(Bullet(self.sw, self.sh, self.player))
                        if self.isSoundOn:
                            self.shoot.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.gameover:
                            if not self.rapidFire:
                                self.playerBullets.append(
                                    Bullet(self.sw, self.sh, self.player)
                                )
                                if self.isSoundOn:
                                    self.shoot.play()
                    if event.key == pygame.K_m:
                        self.isSoundOn = not self.isSoundOn
                    if event.key == pygame.K_TAB:
                        if self.gameover:
                            self.gameover = False
                            self.lives = 3
                            self.asteroids.clear()
                            self.aliens.clear()
                            self.alienBullets.clear()
                            self.stars.clear()
                            if self.score > self.highScore:
                                self.highScore = self.score
                            self.score = 0

            self.redrawGameWindow()

        pygame.quit()


game = Game()
game.run()
