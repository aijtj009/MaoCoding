import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

from random import *
import time

MagicSquare=[[" ",1,2],
             [3,4,5],
             [6,7,8]]

for i in range(100):
    R1=randint(0,2)
    C1=randint(0,2)
    R2=randint(0,2)
    C2=randint(0,2)
    MagicSquare[R1][C1],MagicSquare[R2][C2]=MagicSquare[R2][C2],MagicSquare[R1][C1]
     

def FindingSquare(Obj):
    for i in range(3):
        for j in range(3):
            if MagicSquare[i][j]==Obj:
                  return i,j

print("""
         +---+---+---+        +---+---+---+
         |   | 2 | 1 |        |   | 1 | 2 |
         +---+---+---+        +---+---+---+
Aim:     | 3 | 4 | 5 |   or   | 3 | 4 | 5 |
         +---+---+---+        +---+---+---+
         | 6 | 7 | 8 |        | 6 | 7 | 8 |
         +---+---+---+        +---+---+---+
""")

mRange=[]
for i in range(8):
#    mRange.append(str(i+1))
    mRange.append(i+1)

##Length=486
##Width=378



pygame.init()
#初始化pygame,为使用硬件做准备
size=width,height=486,378
BLACK=0,0,0
WHITE=255,255,255
screen = pygame.display.set_mode(size, 0, 32)
gameDisplay = screen
#创建了一个窗口
pygame.display.set_caption("九宫格八子棋游戏")
#设置窗口标题
background_image_filename = 'BackGroundJieMaChao.png'
mouse_image_filename = 'fugu.png'
#指定图像文件名称
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像
Chess_Sound = pygame.mixer.Sound("FinishTask.wav")
YouWin_Sound = pygame.mixer.Sound("YouWin.wav")
Music = pygame.mixer.music.load("大海.mp3")

NumPic=[]
NumPicRect=[]
for i in range(8): 
    NumPic.append(pygame.image.load(str(i+1)+".png"))
for i in range(8):    
    NumPicRect.append(NumPic[i].get_rect())
pygame.display.set_icon(NumPic[7])  
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def MessageDisplay(text):
    largeText = pygame.font.Font(None,48)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height*2/3))
    gameDisplay.blit(TextSurf, TextRect)
    
def PrintSquare():
    for i in range(3):
        print("+---+---+---+")
        s=""
        for j in range(3):
            s+="| "+str(MagicSquare[i][j])+" "
            if MagicSquare[i][j]!=" ":
                NumPicRect[MagicSquare[i][j]-1].top=i*64
                NumPicRect[MagicSquare[i][j]-1].left=j*64            
        print(s+"|")
    print("+---+---+---+")
    
PrintSquare()
m=9
myText=""
pygame.mixer.music.play(-1)
##Running=True
##while Running:
#游戏主循环
##    rc = (randint(0,255), randint(0,255), randint(0,255))
##    rp = (randint(0,Length), randint(0,Width))
##    rs = (Length-randint(rp[0], Length), Width-randint(rp[1], Width))    
##    pygame.draw.rect(screen, rc, Rect(rp, rs))
fps = 24

def MoveChess():
    print(m)
    SpaceRow,SpaceCol=FindingSquare(" ")
    if m in mRange:
        mRow,mCol=FindingSquare(m)
        if (SpaceRow==mRow and abs(SpaceCol-mCol)==1) or (SpaceCol==mCol and abs(SpaceRow-mRow)==1):
            MagicSquare[SpaceRow][SpaceCol],MagicSquare[mRow][mCol]=MagicSquare[mRow][mCol],MagicSquare[SpaceRow][SpaceCol]
            myText=""
            #pygame.mixer.music.stop()
            pygame.mixer.Sound.play(Chess_Sound)
            PrintSquare()
        else:
            myText="Can't Do.Sorry"
            print(myText)                    
    else:
        myText="Must be in 1..8"
        print(myText)
        
fclock = pygame.time.Clock()
while MagicSquare!=[[" ",1,2],[3,4,5],[6,7,8]] and MagicSquare!=[[" ",2,1],[3,4,5],[6,7,8]]:    
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            #键盘有按下？
            if event.key == K_q:
                m="++"
                print("You just Quit")
                myText="You just Quit"
                MessageDisplay(myText)
                pygame.display.update() 
                time.sleep(5)
                pygame.quit()
                break
            elif event.key == K_1 or event.key == K_KP1:
                m=1
            elif event.key == K_2 or event.key == K_KP2:
                m=2                
            elif event.key == K_3 or event.key == K_KP3:
                m=3
            elif event.key == K_4 or event.key == K_KP4:
                m=4
            elif event.key == K_5 or event.key == K_KP5:
                m=5
            elif event.key == K_6 or event.key == K_KP6:
                m=6
            elif event.key == K_7 or event.key == K_KP7:
                m=7
            elif event.key == K_8 or event.key == K_KP8:
                m=8
            MoveChess()    
        elif event.type == KEYUP:
            #如果用户放开了键盘，图就不要动了
            m=9
            move_x = 0
            move_y = 0
        elif event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0:
                        print('Pressed LEFT Button!')
                    elif index == 1:
                        print('The mouse wheel Pressed!')
                    elif index == 2:
                        print('Pressed RIGHT Button!')
#elif event.type == MOUSEMOTION:
                        #return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            p=mouse_y//64
            q=mouse_x//64
            if 0<=p<=2 and 0<=q<=2:
                m=MagicSquare[p][q]
                if m!=" ":
                    MoveChess()            
    if myText=="You just Quit":
        break
    screen.blit(background, (0,0))
    #将背景图画上去 
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
             
#    screen.fill(WHITE)
    MessageDisplay(myText)
    for i in range(8):
        screen.blit(NumPic[i],NumPicRect[i])  
    pygame.display.update()
    #刷新一下画面
    fclock.tick(fps)

if m!="++":
    myText="You have passed! :-)"
    print(myText)
    MessageDisplay(myText)
    pygame.display.update()
    pygame.mixer.Sound.play(YouWin_Sound)
    time.sleep(9)
    pygame.quit()
