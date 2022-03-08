from ursina import *

app= Ursina()
spaceship = Entity(model = 'quad', collider= 'box', texture= 'textures/spaceship.png' , position = (-6.2,0))
monster = Entity(model = 'quad' , collider= 'box', texture= 'textures/monster.png', position= (8 , random.randint(-3 , 3), 0))
background = Entity(model = 'quad' , texture= 'textures/backgroundtxt.jpg' , scale= (20,10) , position= (0,0,1))
bullet= Entity(model= 'quad' , collider= 'box', texture='textures/bullet.png' , scale= (0.4, 0.4) , position= (-6.5,0, 0) , visible= False)

fire_sound= Audio('audio/fire.wav', loop= False, autoplay= False)
bang_sound= Audio('audio/bang.wav', loop= False, autoplay= False)
theme_song= Audio('audio/themesong.wav', loop=True, autoplay=True)
score= 0

window.title = 'BattleSpace'                
window.borderless = False               
window.fullscreen = False              
window.exit_button.visible = False     
window.fps_counter.enabled = False



def update():
    global score 
    Text(text= score)
    if monster.intersects(bullet).hit:
        score += 1
        monster.animate_position(monster.position+(monster.right*40), curve=curve.linear, duration=0.1)
        bang_sound.play()        
        bullet.position = (-6.5, spaceship.y , 0.1)
        bullet.visible = False
    if bullet.x != -6.5:
        bullet.position = (-6.5, spaceship.y , 0.1)
    if bullet.y != spaceship.y:
        bullet.y = spaceship.y
    if held_keys['w'] and spaceship.y < 3:
        spaceship.y += 4 * time.dt
    if held_keys['s'] and spaceship.y > -3:
        spaceship.y -= 4 * time.dt 
    if held_keys['w'] and bullet.y < 3:
        bullet.y += 4 * time.dt
    if held_keys['s'] and bullet.y > 3:
        bullet.y -= 4 * time.dt
    if monster.x < -8:
        monster.position = (8 , random.randint(-3 , 3) , 0.1)
        monster.animate_position(monster.position+(monster.left*40), curve=curve.linear, duration=10)
    if monster.x > 8:
         monster.position = (8 , random.randint(-3 , 3), 0.1)
         monster.animate_position(monster.position+(monster.left*40), curve=curve.linear, duration=10)

    if spaceship.intersects(monster).hit:
        bang_sound.play()
        Text(text='GAME OVER', scale=2, position= (-0.1,0,0))
        destroy(spaceship)
        destroy(monster)
        destroy(bullet)



       
        
monster.animate_position(monster.position+(monster.left*40), curve=curve.linear, duration=10)


def input(key):
    if key == 'space':
        fire_sound.play()
        bullet.visible= True
        bullet.animate_position(bullet.position+(bullet.right*30), curve=curve.linear, duration=1)

app.run()
