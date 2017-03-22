from gamelib import *

game = Game(800,600,"Protecting POTUS")


bk = Image("POTUS\\whitehouse.gif",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)


obama = Image("POTUS\\obama.gif", game)
obama.setSpeed(4,60)
obama.moveTo(200, 200)
         

cops = [] #Empty List

for times in range(50):
   cops.append( Image("POTUS\\cop2.png", game) )

for c in cops:
   x = randint(100,700)
   y = -randint(100,5000)
   s = randint(1,3)
   c.moveTo(x,y)
   c.setSpeed(s,180)
   c.resizeBy(-70)

trump = Image("POTUS\\trump.gif",game)
trump.resizeBy(-25)

explosion = Animation("POTUS\\explosion.png",22,game, 285/5, 320/5)
explosion.visible = False
brick = Image("POTUS\\brick.png", game)
brick.resizeBy(-90)

brick.visible = False

bk.draw()
game.drawText("Protecting POTUS",game.width/4 ,game.height/4,Font(blue,90,red))
game.drawText("by DJ Inc.",game.width/5,game.height/5, Font(red, blue))
game.drawText("Instructions : AIM WITH THE ARROW KEYS SHOOT WITH THE SPACEBAR",game.width/12 ,game.height/2.3,Font(black,30,black))
game.drawText("TO DEFEND TRUMP AGAINST ALL ENEMIES",game.width/12 ,game.height/2.1,Font(black,30,black))
game.drawText("Press [SPACE] to Begin",game.width/2 + 80,game.height - 50,Font(black,40,white))
game.update()
game.wait(K_SPACE)
game.drawBackground()
trump.draw()
game.update()

game.wait(K_SPACE)

shoot = Sound("sound\\blaster.wav",1)
boom = Sound("sound\\Arcade Explo A.wav",3)

while not game.over:
   game.processInput()
   game.scrollBackground("down",1)

   obama.move(True)
   trump.move()
   explosion.draw(False) 
   brick.move()

   for c in cops:
       c.move()
       if c.collidedWith(brick):
           c.visible = False
           explosion.visible = True
           explosion.moveTo(c.x,c.y)
           boom.play()
           obama.health -= 5

       if c.collidedWith(trump):
           trump.health -= 10
           explosion.visible = True
           explosion.moveTo(trump.x,trump.y)
           boom.play()
           c.visible = False
           
       

   if trump.health == 0:
       game.over = True
   if obama.health == 0:
       game.over = True
   
   if keys.Pressed[K_LEFT] or joy.pad[E]:
       trump.rotateBy(2,"left")
   if keys.Pressed[K_RIGHT] or joy.pad[W]:
       trump.rotateBy(2,"right")
   if keys.Pressed[K_UP] or joy.button[4]:
      trump.forward(2)
   else:
         trump.speed *= 0.99
       
   if keys.Pressed[K_SPACE] or joy.button[5]:
       brick.visible = True
       brick.moveTo(trump.x,trump.y)

       brick.setSpeed(10 , trump.getAngle())
       shoot.play()

   game.drawText("Obama HP: " + str(obama.health),5,5)
   game.drawText("Trump HP: " + str(trump.health),155,5)
   game.update(60)

game.drawText("Game Over",game.width/4,game.height/3,Font(red,90,black))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(blue,40,black))
game.update()
game.wait(K_ESCAPE)

game.over = True

#while not game.over:
#game.quit gets removed where it says game.over = true change it to game = false then start other loop/level
