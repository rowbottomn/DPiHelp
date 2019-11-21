import  sys
#from pygame.locals import *

pygame.init()
pygame.mixer.init()

#global variables
mixer = pygame.mixer

music = pygame.music

songs = []

activeSong = 0

def check_keys():
    global songs, activeSong, music, mixer
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (activeSong < 0):
                    activeSong -= 1  
                else:
                    activeSong = len(songs)-1

            if event.key == pygame.K_RIGHT:
                if (activeSong > len(songs)-1):
                    activeSong += 1  
                else:
                    activeSong = 0
            if event.key == pygame.K_UP:
                if (music.getBusy()):
                  music.pause()
                else:
                  music.play()

            #if event.key == pygame.K_DOWN:


            # https://www.pygame.org/docs/ref/key.html  
            #if event.key == pygame.K_z:
            

print("welcome")
print("loading")
pygame.mixer.music.load("allforone.mp3")
print("Now Playing: All for one")
pygame.mixer.music.play(loops=0, start=0.0)

while pygame.mixer.music.get_busy ==True: #or interupt:
  continue