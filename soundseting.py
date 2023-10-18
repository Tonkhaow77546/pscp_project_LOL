import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

class Buttonn(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Buttonn, self).__init__()

		self.image = img
		self.scale = scale
		self.image = pygame.transform.scale(self.image, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action

pygame.mixer.init()
pygame.mixer.music.load("UI/music1.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

on = pygame.image.load('UI/soundOnBtn.png')
off = pygame.image.load('UI/soundOffBtn.png')


sound_btn = Buttonn(on, (24, 24), 250, 50) ##2 อันท้าย เป็นตน.นะ

sound_on = False

running = True
while running:
	win.fill((32, 32, 32))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q or \
				event.key == pygame.K_ESCAPE:
				running = False

	if sound_btn.draw(win):
		sound_on = not sound_on
		
		if sound_on:
			sound_btn.update_image(on)
			pygame.mixer.music.set_volume(0.7)
		else:
			sound_btn.update_image(off)
			pygame.mixer.music.set_volume(0)
	pygame.display.update()

pygame.quit()