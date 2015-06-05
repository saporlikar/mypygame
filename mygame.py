import pygame, sys
from pygame.locals import *
import random

BLACK=(0,0,0)
WHITE=(255,255,255)
BROWN=(153,76,0)
GREEN=(0,255,0)
BLUE =(0,0,255)


DIRT =0
GRASS=1
WATER=2
COAL =3
CLOUD=4

cloudx=-200
cloudy=0

resources=[DIRT,GRASS,WATER,COAL]

textures={
			DIRT :pygame.image.load("Dirt.png"),
			GRASS:pygame.image.load("Grass.png"),
			WATER:pygame.image.load("Water.png"),
			COAL :pygame.image.load("Coal.png"),
			CLOUD:pygame.image.load("cloud.png")
		}
fpsClock=pygame.time.Clock()

TILESIZE=40
MAPWIDTH=15
MAPHEIGHT=15

tilemap = [ [random.choice(resources) for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ] 

for row in range(MAPHEIGHT):
	for column in range(MAPWIDTH):
		randomNumber=random.randint(0,15)
		if(randomNumber==0):
			tile=COAL
		elif(randomNumber==1 or randomNumber==2):
			tile=WATER
		elif(randomNumber>=3 and randomNumber<=7):
			tile=GRASS
		else:
			tile=DIRT
		tilemap[row][column]=tile



#tilemap=[
#			[GRASS,COAL,DIRT],
#			[WATER,WATER,GRASS],
#			[COAL,GRASS,WATER],
#			[DIRT,GRASS,COAL],
#			[GRASS,WATER,DIRT]
#		]

inventory={
				DIRT:0,
				GRASS:0,
				WATER:0,
				COAL:0
		   }

pygame.init()

pygame.display.set_caption('M I N E C R A F T -- 2 D')
pygame.display.set_icon(pygame.image.load('player1.png'))

INVFONT=pygame.font.Font("freesansbold.ttf",18)

DISPLAYSURF=pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+70))

PLAYER=pygame.image.load("player1.png").convert_alpha()
playerPos=[0,0]

while True:
	for event in pygame.event.get():
#		print(event)
		if (event.type==QUIT):
			pygame.quit()
			sys.exit()
		elif (event.type==KEYDOWN):
			if(event.key==K_RIGHT and playerPos[0]<MAPWIDTH-1):
				playerPos[0]+=1
			elif(event.key==K_DOWN and playerPos[1]<MAPHEIGHT-1):
				playerPos[1]+=1
			elif(event.key==K_LEFT and playerPos[0]>0):
				playerPos[0]-=1
			elif(event.key==K_UP and playerPos[1]>0):
				playerPos[1]-=1
			elif(event.key==K_SPACE):
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile]+=1
				tilemap[playerPos[1]][playerPos[0]]=DIRT
#					print(inventory)
			elif(event.key==K_1):
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				if(inventory[DIRT]>0):
					inventory[DIRT]-=1
					tilemap[playerPos[1]][playerPos[0]]=DIRT
					inventory[currentTile]+=1
			elif(event.key==K_2):
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				if(inventory[GRASS]>0):
					inventory[GRASS]-=1
					tilemap[playerPos[1]][playerPos[0]]=GRASS
					inventory[currentTile]+=1
			elif(event.key==K_3):
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				if(inventory[WATER]>0):
					inventory[WATER]-=1
					tilemap[playerPos[1]][playerPos[0]]=WATER
					inventory[currentTile]+=1
			elif(event.key==K_1):
				currentTile=tilemap[playerPos[1]][playerPos[0]]
				if(inventory[COAL]>0):
					inventory[COAL]-=1
					tilemap[playerPos[1]][playerPos[0]]=COAL
					inventory[currentTile]+=1


	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))
	
	placePosition=10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+15))
		placePosition+=45
		textObj=INVFONT.render(str(inventory[item]),True,WHITE,BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+30))
		placePosition+=80

	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE+5,playerPos[1]*TILESIZE+5))

	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
	cloudx+=1
	if(cloudx>MAPWIDTH*TILESIZE):
		cloudx=-200
		cloudy=random.randint(0,MAPHEIGHT*TILESIZE)

	pygame.display.update()
	fpsClock.tick(2000)
