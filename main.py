import pygame
import time
pygame.init()


#global variables
print("welcome")
print("loading")
pygame.mixer.music.load("allforone.mp3")
print("Now Playing: All for one")
pygame.mixer.music.play(loops=0, start=0.0)

while pygame.mixer.music.get_busy ==True: #or interupt:
  continue


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("bloodshot.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Bloodshot")

while pygame.mixer.music.get_busy == True:
  continue


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("breakthisdown.mp3")
pygame.mixer.music.play(loops=0, start=0.2)
print("Now Playing: Break This Down")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("cantbackdown.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Can't Back Down")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("jollytothecore.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Jolly to the Core")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("leaveitalltoshine.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print ("Now Playing: Leave it all to Shine")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("nightfalls.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Nightfalls")

while pygame.mixer.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("outlaws.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Outlaws")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("Queen-of-Mean.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Queen of Mean")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("seventeen.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Seventeen (Riverdale Version)")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("tomholland.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing Singing in the Rain/ Umbrella Mashup")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("youandme.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: You and Me (Descendants 2)")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("Intotheunknown.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Into the Unknown (P!ATD version)")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("fathoms.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Fathoms Below (Live version)")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)


print("loading")
pygame.mixer.music.unload()
pygame.mixer.music.load("unfortunate.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
print("Now Playing: Poor Unfortunate Souls (Live Version)")

while pygame.mixer.music.get_busy ==True:
  time.sleep(3)

