import keyboard
import time
import random
import copy
import os

block1 = [[-1,4,1],[0,4,1],[-1,5,1],[0,5,1]] #O
block2 = [[0,4,2],[0,5,2],[0,6,2],[-1,5,2],[0,5]] #T
block3 = [[-1,3,3],[-1,4,3],[-1,5,3],[-1,6,3],[-0.5,4.5]] #I
block4 = [[0,4,4],[0,5,4],[0,6,4],[-1,4,4],[0,5]] #J
block5 = [[-1,6,5],[0,4,5],[0,5,5],[0,6,5],[0,5]] #L
block6 = [[-1,4,6],[-1,5,6],[0,5,6],[0,6,6],[0,5]] #Z
block7 = [[0,4,7],[0,5,7],[-1,5,7],[-1,6,7],[0,5]] #S
blocks =[block1,block2,block3,block4,block5,block6,block7]

roundblock=[[[[0,-1],[-1,0],[0,1]],[[-1,0],[0,1],[1,0]],[[0,1],[1,0],[0,-1]],[[1,0],[0,-1],[-1,0]]],
[[[-0.5,-1.5],[-0.5,-0.5],[-0.5,0.5],[-0.5,1.5]],[[-1.5,0.5],[-0.5,0.5],[0.5,0.5],[1.5,0.5]],[[0.5,-1.5],[0.5,-0.5],[0.5,0.5],[0.5,1.5]],[[-1.5,-0.5],[-0.5,-0.5],[0.5,-0.5],[1.5,-0.5]]],
[[[-1,-1],[0,-1],[0,1]],[[-1,1],[-1,0],[1,0]],[[0,-1],[0,1],[1,1]],[[-1,0],[1,0],[1,-1]]],
[[[-1,1],[0,1],[0,-1]],[[1,0],[-1,0],[1,1]],[[0,-1],[0,1],[1,-1]],[[1,0],[-1,0],[-1,-1]]],
[[[-1,-1],[-1,0],[0,1]],[[-1,1],[0,1],[1,0]],[[0,-1],[1,0],[1,1]],[[1,-1],[0,-1],[-1,0]]],
[[[0,-1],[-1,0],[-1,1]],[[-1,0],[0,1],[1,1]],[[1,-1],[1,0],[0,1]],[[-1,-1],[0,-1],[1,0]]]]

SRS =[[[0,0],[0,1],[-1,1],[2,0],[2,1]],[[0,0],[0,-1],[-1,-1],[2,0],[2,-1]],[[0,0],[0,-1],[1,-1],[-2,0],[-2,-1]],[[0,0],[0,1],[1,1],[-2,0],[-2,1]]]
SRSofI =[[[0,0],[0,-1],[0,2],[-2,-1],[1,2]],[[0,0],[0,-2],[0,1],[1,-2],[-2,1]],[[0,0],[0,1],[0,-2],[1,2],[-1,-2]],[[0,0],[0,2],[0,-1],[-1,2],[2,-1]]]

location=[]
moveblock=[]
supports=[]
hold=[]

def printboad():
    boad = ""
    boad += ("⬜"*12+"     NEXT "+str(num+1) +"\n")
    for i in range(22):
        boad += ("⬜")
        for j in range(10):
            ad = [l for l in location + moveblock if l[0] ==i and l[1]==j]
            if ad:
                if ad[0][2] ==0:
                    boad += ("💥")
                else:
                    boad += (chr(128996+ad[0][2]))
            else:
                ae = [m for m in supports if m[0] ==i and m[1]==j]
                if ae:
                    boad += ("⬛")
                else:
                    boad += ("  ")
        boad += ("⬜  ")
        if i < 2:
            for j in range(3,7):
                af = [l for l in nex[num%20] if l[0] ==i-1 and l[1]==j]
                if af:
                    boad += (chr(128996+af[0][2]))
                else:
                    boad += ("  ")
        elif i == 3:
            boad += (" 👆👆👆 "+str(num+2))
        elif i <6:
            for j in range(3,7):
                af = [l for l in nex[(num+1)%20] if l[0] ==i-5 and l[1]==j]
                if af:
                    boad += (chr(128996+af[0][2]))
                else:
                    boad += ("  ")
        elif i == 7:
            boad += (" 👆👆👆 "+str(num+3))
        elif i <10:
            for j in range(3,7):
                af = [l for l in nex[(num+2)%20] if l[0] ==i-9 and l[1]==j]
                if af:
                    boad += (chr(128996+af[0][2]))
                else:
                    boad += ("  ")
        elif i == 12:
            boad += (" LEVEL =>"+str(level))
        elif i ==14:
            boad += (" LINES =>"+str(lines))
        elif i == 16:
            boad += (" SCORE =>"+str(score))
        elif i == 18:
            boad += (" -HOLD-")
        elif i <21:
            for j in range(3,7):
                af = [l for l in hold if l[0] ==i-20 and l[1]==j]
                if af:
                    boad += (chr(128996+af[0][2]))
                else:
                    boad += ("  ")
        elif i == 21:
            boad += (" ------")
        boad += ("\n")
    boad += ("⬜"*12)
    os.system('cls')
    print(boad)
    
#location=[[21,2,1],[20,2,2],[21,1,3],[21,3,4],[20,3,5],[19,3,6],[19,4,7],[20,4,1],[16,5,2],[19,6,3],[20,6,4],[21,7,5],[21,6,6]]

angle = 0
num=1
def setblock(block):
    global moveblock,angle,nex
    moveblock.extend(block)
    angle = 0
    supportdisplay()
    if num%20==13:
        nex =[(random.choice(blocks) if i < 10 else nex[i]) for i in range(20)]
    elif num%20==3:
        nex =[(random.choice(blocks) if i >= 10 else nex[i]) for i in range(20)]

def fallblock():
    global moveblock
    for i in moveblock:
        i[0] +=1

def stopfall():
    for i in moveblock:
        aa = [j for j in location if (j[0] ==i[0]+1 and j[1]==i[1])]
        if len(aa)>0 or i[0] >=21:
            return True
    return False

lines = 0
score = 0
def removeline():
    global location,lines,score,level,supports
    lines_first = lines
    L = []
    for i in range(22):
        a = [False for l in range(10)]
        for j in range(10):
            ab = [k for k in location if k[0]==i and k[1]==j]
            if len(ab) >0:
                a[j] = True
        if all(a):
            location = [l for l in location if l[0] != i]
            location.extend([[i,k,0] for k in range(10)])
            L.append(i)
            lines += 1
            if mode == "easy":
                if lines % 10 == 0:
                    level += 1
            elif mode == "nomal":
                if lines % 8 == 0:
                    level += 1
            elif mode == "hard":
                if lines % 5 == 0:
                    level += 1
    if L:
            printboad()
            time.sleep(0.15)
            location = [l for l in location if l[0] not in L]
            supports = []
            printboad()
            time.sleep(0.15)
            for j in L:
                for m in location:
                    if m[0] < j:
                        m[0] += 1
            time.sleep(0.15)
            printboad()
    lines_final = lines
    score += (lines_final-lines_first)**2*100*(level+1)

def supportdisplay():
    global supports
    z = copy.deepcopy(moveblock)
    while True:
        d = True
        for i in z:
            aa = [j for j in location if (j[0] ==i[0]+1 and j[1]==i[1])]
            if len(aa)>0 or i[0] >=21:
                d = False
                break
        if not d:
            supports = [[z[0][0],z[0][1],8],[z[1][0],z[1][1],8],[z[2][0],z[2][1],8],[z[3][0],z[3][1],8]]
            break
        else:
            for i in z:
                i[0] +=1

def right():
    global moveblock
    ok = True
    for i in moveblock:
        aa = [j for j in location if (j[1] ==i[1]+1 and j[0]==i[0])]
        if len(aa)>0 or i[1] >=9:
            ok = False
    if ok:
        for j in moveblock:
            j[1] +=1
        supportdisplay()
        printboad()

def left():
    global moveblock
    ok = True
    for i in moveblock:
        aa = [j for j in location if (j[1] ==i[1]-1 and j[0]==i[0])]
        if len(aa)>0 or i[1] <=0:
            ok = False
    if ok:
        for j in moveblock:
            j[1] -=1
        supportdisplay()
        printboad()

def down():
    global moveblock
    ok = True
    for i in moveblock:
        aa = [j for j in location if (j[0] ==i[0]+1 and j[1]==i[1])]
        if len(aa)>0 or i[0] >=21:
            ok = False
    if ok:
        for j in moveblock:
            j[0] +=1
        printboad()

def turn(direction):
    global moveblock,angle
    col = moveblock[0][2]
    if col > 1:
        angle_before = angle
        if direction == "left":
            angle = angle-1 if angle >0 else 3
        elif direction == "right":
            angle = angle+1 if angle <3 else 0
        e = roundblock[col-2][angle]
        if col != 3:
            SRSn = (3 if angle_before == 1 else 2)if angle_before%2==1 else(1 if angle == 1 else 0)
            n = 0
            while True:
                m = [[moveblock[4][0]+e[0][0]+SRS[SRSn][n][0],moveblock[4][1]+e[0][1]+SRS[SRSn][n][1]],
                                [moveblock[4][0]+e[1][0]+SRS[SRSn][n][0],moveblock[4][1]+e[1][1]+SRS[SRSn][n][1]],
                                [moveblock[4][0]+e[2][0]+SRS[SRSn][n][0],moveblock[4][1]+e[2][1]+SRS[SRSn][n][1]],
                                [moveblock[4][0]+SRS[SRSn][n][0],moveblock[4][1]+SRS[SRSn][n][1]]]
                ac = [j for j in location if (j[0] ==m[0][0] and j[1] ==m[0][1])or(j[0] ==m[1][0] and j[1] ==m[1][1])or
                    (j[0] ==m[2][0] and j[1] ==m[2][1])or(j[0] ==m[3][0] and j[1] ==m[3][1])]
                
                if len(ac) ==0 and max(m[0][1],m[1][1],m[2][1],m[3][1])<=9 and min(m[0][1],m[1][1],m[2][1],m[3][1])>=0 and max(m[0][0],m[1][0],m[2][0],m[3][0])<=21:
                    moveblock = [[m[0][0],m[0][1],col],[m[1][0],m[1][1],col],[m[2][0],m[2][1],col],[m[3][0],m[3][1],col],m[3]]
                    supportdisplay()
                    printboad()
                    break
                elif n==4:
                    break
                else:
                    n += 1
        elif col ==3:
            if angle_before == 0:
                if angle == 1:
                    SRSn = 1
                else: 
                    SRSn = 0
            elif angle_before == 1:
                if angle ==0:
                    SRSn = 3
                else: 
                    SRSn = 0
            elif angle_before == 2:
                if angle == 1:
                    SRSn = 2
                else:
                    SRSn = 3
            else:
                if angle ==0:
                    SRSn = 2
                else:
                    SRSn = 1
            n = 0
            while True:
                m = [[round(moveblock[4][0]+e[0][0]+SRSofI[SRSn][n][0]),round(moveblock[4][1]+e[0][1]+SRSofI[SRSn][n][1])],
                                [round(moveblock[4][0]+e[1][0]+SRSofI[SRSn][n][0]),round(moveblock[4][1]+e[1][1]+SRSofI[SRSn][n][1])],
                                [round(moveblock[4][0]+e[2][0]+SRSofI[SRSn][n][0]),round(moveblock[4][1]+e[2][1]+SRSofI[SRSn][n][1])],
                                [round(moveblock[4][0]+e[3][0]+SRSofI[SRSn][n][0]),round(moveblock[4][1]+e[3][1]+SRSofI[SRSn][n][1])]]
                ac = [j for j in location if (j[0] ==m[0][0] and j[1] ==m[0][1])or(j[0] ==m[1][0] and j[1] ==m[1][1])or
                    (j[0] ==m[2][0] and j[1] ==m[2][1])or(j[0] ==m[3][0] and j[1] ==m[3][1])]
                
                if len(ac) ==0 and max(m[0][1],m[1][1],m[2][1],m[3][1])<=9 and min(m[0][1],m[1][1],m[2][1],m[3][1])>=0 and max(m[0][0],m[1][0],m[2][0],m[3][0])<=21:
                    moveblock = [[m[0][0],m[0][1],col],[m[1][0],m[1][1],col],[m[2][0],m[2][1],col],[m[3][0],m[3][1],col],[moveblock[4][0]+SRSofI[SRSn][n][0],moveblock[4][1]+SRSofI[SRSn][n][1]]]
                    supportdisplay()
                    printboad()
                    break
                elif n==4:
                    break
                else:
                    n += 1

def holding():
    global hold,moveblock,canhold,num
    if not hold:
        hold =blocks[moveblock[0][2]-1][:]
        moveblock = []
        setblock(copy.deepcopy(nex[num%20]))
        canhold = True
        num += 1
    else:
        if canhold:
            #print(blocks,moveblock)
            hold , moveblock = copy.deepcopy(blocks[moveblock[0][2]-1]) , copy.deepcopy(hold)
            canhold = False
            supportdisplay()
        else:
            return
    printboad()

modes = ["easy","nomal","hard"]
def printtitle():
    title = (("  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟"if A else "🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟")+"\n"+
            ("🌟"if A else"  ")+"🟥🟥🟥🟧🟧🟧🟨🟨🟨🟩🟩   🟦   🟪🟪"+("🌟"if A else"  ")+"\n"+
            ("  "if A else"🌟")+"  🟥  🟧      🟨  🟩  🟩 🟦 🟪    "+("  "if A else"🌟")+"\n"+("🌟"if A else"  ")+"  🟥  🟧🟧🟧  🟨  🟩🟩   🟦   🟪  "+("🌟"if A else"  ")+"\n"+
            ("  "if A else"🌟")+"  🟥  🟧      🟨  🟩 🟩  🟦     🟪"+("  "if A else"🌟")+"\n"+("🌟"if A else"  ")+"  🟥  🟧🟧🟧  🟨  🟩  🟩 🟦 🟪🟪  "+("🌟"if A else"  ")+"\n"+
            ("  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟"if A else "🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟  🌟")+"\n"+"  SELECT MODE!!"+"\n"*2)
    
    if A and mode == "easy":
        title += "👉"
    else: title += "  "
    title += ((("  EASY MODE!!!!🌶️" +"\n"+"      level : 0 ~  level up speed : low")if mode == "easy" else "     ・EASY MODE") + "\n"*2)
    if A and mode == "nomal":
        title += "👉"
    else: title += "  "
    title += ((("  NOMAL MODE!!!!🌶️🌶️" +"\n"+"      level : 5 ~  level up speed : medium")if mode == "nomal" else "     ・NOMAL MODE") + "\n"*2)
    if A and mode == "hard":
        title += "👉"
    else: title += "  "
    title += ((("  HARD MODE!!!!🌶️🌶️🌶️" +"\n"+"      level : 10 ~  level up speed : high")if mode == "hard" else "     ・HARD MODE") + "\n"*2)
    os.system("cls")
    print(title)

def gameover():
    global location,supports
    for i in range(22):
        supports.extend([x for x in location if x[0] == i])
        location = [x for x in location if x[0] != i]
        printboad()
        time.sleep(0.1)
    location = [[x[0], x[1], 0 ]for x in supports]
    printboad()
    time.sleep(0.1)
    location = []
    supports = []
    printboad()
    location = [[0,0,1],[1,0,1],[2,0,1],[3,0,1],[3,1,1],[3,2,1],[3,3,1],[2,3,1],[0,1,1],[0,2,1],
            ]
    return



b = False
n = 0
A = True
mode = modes[0]
while True:
    t1 = time.time()
    printtitle()
    while time.time()-t1<0.5:
        if keyboard.is_pressed("down"):
            if n < 2:
                n += 1
                mode = modes[n]
                printtitle()
                time.sleep(0.1)
        elif keyboard.is_pressed("up"):
            if n > 0:
                n -= 1
                mode = modes[n]
                printtitle() 
                time.sleep(0.1)
        elif keyboard.is_pressed("enter"):
            b = True
            break
    if b:
        break
    A ^= True
    
level = 0 if mode == "easy" else(5 if mode == "nomal" else 10)
            
nex =[random.choice(blocks) for i in range(20)]
#nex =[block2 for i in range(200)]
setblock(copy.deepcopy(nex[0]))

#location = [[0,0,1],[1,0,1],[2,0,1],[3,0,1],[3,1,1],[3,2,1],[3,3,1],[2,3,1],[0,1,1],[0,2,1],
#            [4,3,2],[5,3,2],[6,3,2],[3,4,2],[3,5,2],[4,6,2],[5,6,2],[6,6,2],[5,5,2],[5,4,2],
#            []]
printboad()
#exit()


while True:
    if stopfall():
        if min(moveblock[i][0] for i in range(len(moveblock))) <2:
            printboad
            location.append(moveblock)
            moveblock = []
            gameover()
            break
        moveblock = [x for x in moveblock if len(x) != 2]
        location.extend(moveblock)
        location
        moveblock = []
        removeline()
        setblock(copy.deepcopy(nex[num%20]))
        canhold = True
        num += 1
    fallblock()
    printboad()
    t = time.time()
    while time.time()-t<2/(level+4)+(0.03 if mode == "hard" else(0.1 if mode == "nomal" else 0.2)):
        if keyboard.is_pressed("d"):
            left()
            time.sleep(0.1)
        elif keyboard.is_pressed("f"):
            right()
            time.sleep(0.1)
        elif keyboard.is_pressed("v"):
            down()
            time.sleep(0.05)
        elif keyboard.is_pressed("j"):
            turn("left")
            time.sleep(0.13)
        elif keyboard.is_pressed("k"):
            turn("right")
            time.sleep(0.13)
        elif keyboard.is_pressed("space"):
            moveblock = [[supports[0][0],supports[0][1],moveblock[0][2]],[supports[1][0],supports[1][1],moveblock[0][2]],[supports[2][0],supports[2][1],moveblock[0][2]],[supports[3][0],supports[3][1],moveblock[0][2]]]
            printboad()
            time.sleep(0.1)
            break
        elif keyboard.is_pressed("h"):
            holding()
            time.sleep(0.1)
        elif keyboard.is_pressed("p"):
            print("NOW POSING")
            p = input("to resume the game, pless enter!\n")