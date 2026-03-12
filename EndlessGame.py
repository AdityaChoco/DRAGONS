import pgzrun, pyautogui, random
WIDTH, HEIGHT=pyautogui.size()
TITLE="EndlessGame"

score=0
lives=3
fire=[]
player=Actor('dragonn.png')
player.pos=(100,HEIGHT/2)
enemies=[]
game_state="Start"
def create_enemies():
    if game_state=="Play":
        enemy=Actor('unicornn.png')
        enemy.pos=(WIDTH,random.randint(0,HEIGHT-10))
        enemies.append(enemy)




def draw():
    screen.clear()
    screen.blit("purple_sky.jpg",(0,0))
    player.draw()
    if game_state=="Start":
        screen.draw.text("Press space to start the game\n Use left and right arrow keys to move\n Collect all the coins\n Do NOT touch the enemies",center=(WIDTH/2,HEIGHT/2))
    elif game_state=="Play":
        for i in enemies:
            i.draw()
        for i in fire:
            i.draw()
        screen.draw.text(f"score --> {score}",(50,50))
        screen.draw.text(f"lives --> {lives}",(WIDTH-200,50))
    else:
        screen.draw.text("Better luck next time :(",center=(WIDTH/2,HEIGHT/2))

def update():
    global game_state,score,lives
    if keyboard.space and game_state=="Start":
        game_state="Play"
    if game_state=="Play":
        if keyboard.up and player.y>10:
            player.y-=10
        if keyboard.down and player.y<HEIGHT-10:
            player.y+=10

        for i in enemies:
            i.x-=10
            if i.x<0:
                enemies.remove(i)
            if i.colliderect(player):
                enemies.remove(i)
                lives-=1
                if lives==0:
                    game_state="End"
                    player.image="skulll.png"
                continue
            



        for i in fire:
            i.x+=10
            if i.x>WIDTH:
                fire.remove(i)
            for u in enemies:
                if i.colliderect(u):
                    enemies.remove(u)
                    fire.remove(i)
                    score+=1
                    break
        if random.randint(0,100)<2:
            create_enemies()

def on_key_down(key):
    global score,lives,game_state,enemies,fire
    if key==keys.RIGHT and game_state=="Play":
        fireball=Actor("fireball.png")
        fireball.pos=player.x+player.width/2,player.y+10
        fire.append(fireball)
    if key==keys.SPACE and game_state=="End":
        game_state="Start"
        lives=3
        score=0
        enemies=[]
        fire=[]
        player.image="dragonn.png"

pgzrun.go()