#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: vargash1
# @Date:   2015-09-18 19:06:48
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last Modified by:   vargash1
# @Last Modified time: 2015-09-18 19:10:09
import pygame
from pygame.locals import*
pygame.init()
import collections
import sys
import os
from random import*
from graphicsPy3 import*

#  for board
def give_rand_int(range1, range2):
    return randint(range1,range2)

def draw_sq(x1, y1, size, win):
    redp = Rectangle(Point(x1,y1),Point(x1 + size, y1 + size))
    redp.setOutline("black")
    redp.draw(win)  
def adjust(temp_val):
    tempval = ((50*temp_val) - 25)
    return tempval
def check_position_horizontal(dictionary,x,y,size):
    flag = False
    for i in range(size):
        is_free = int(str(x) + str(y))
        if dictionary[is_free] == "empty":
            x += 1
        elif dictionary[is_free] == "ship":
            flag = True
            break

    return flag;
def check_position_vertical(dictionary ,x,y,size):
    flag = False
    for i in range(size):
        is_free = int(str(x) + str(y))
        if dictionary[is_free] == "empty":
            y += 1
        elif dictionary[is_free] == "ship":
            flag = True
            break
    return flag

def randomize_AircraftCarry(dictionary):
    # horizontal or vertical ship is based of rand boolean
    direction = choice([True,False])
    #this randoms with ship being in hori position
    if direction == True:
        temp_x = randint(3,8)
        temp_y= temp_x
        #chck this
        temp_x -=2
        if (check_position_horizontal(dictionary,temp_x,temp_y,5)):
            randomize_AircraftCarry(dictionary)
        elif not(check_position_horizontal(dictionary,temp_x,temp_y,5)):     
            for i in range(5):
                add = int(str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_x +=1
    #vertical
    elif direction != True:
        temp_y = randint(3,8)
        temp_y -= 2
        temp_x = temp_y
        if (check_position_vertical(dictionary,temp_x,temp_y,5)):
            randomize_AircraftCarry(dictionary)
        elif not(check_position_vertical(dictionary,temp_x,temp_y,5)):
            for i in range (5):
                add = int(str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_y += 1
def randomize_Battleship(dictionary):
    direction = choice([True,False])
    if direction == True:
        temp_x = randint(2,8)
        temp_x -= 1
        temp_y = temp_x
        if (check_position_horizontal(dictionary,temp_x,temp_y,4)):
            randomize_Battleship(dictionary)
        elif not(check_position_horizontal(dictionary,temp_x,temp_y,4)):
            for i in range(4):
                add = int (str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_x += 1
    elif direction != True:
        temp_y  = randint(2,8)
        temp_y -=1
        temp_x = temp_y
        if (check_position_vertical(dictionary,temp_x,temp_y,4)):
            randomize_Battleship(dictionary)
        elif not(check_position_vertical(dictionary,temp_x,temp_y,4)):
            for i in range(4):
                add = int(str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_y += 1
def randomize_Submarine(dictionary):
    direction = choice([True,False]) 
    if direction == True:
        temp_x = randint(2,9)
        temp_x -= 1
        temp_y = temp_x
        if (check_position_horizontal(dictionary,temp_x,temp_y,3)):
            randomize_Submarine(dictionary)
        elif not(check_position_horizontal(dictionary,temp_x,temp_y,3)):
            for i in range (3):
                add = int(str(temp_x)+ str(temp_y))
                dictionary[add] = "ship"
                temp_x +=1
    elif direction != True:
        temp_y = randint(2,9)
        temp_y -= 1
        temp_x = temp_y
        if (check_position_vertical(dictionary,temp_x,temp_y,3)):
            randomize_Submarine(dictionary)
        elif not(check_position_vertical(dictionary,temp_x,temp_y,3)):
            for i in range(3):
                add = int(str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_y += 1
def randomize_PatrolShip(dictionary):
    direction = choice([True,False])
    if direction == True:
        temp_x = randint(2,10)
        temp_x -= 1
        temp_y = temp_x
        if (check_position_horizontal(dictionary,temp_x,temp_y,2)):
            randomize_PatrolShip(dictionary)
        elif not(check_position_vertical(dictionary,temp_x,temp_y,2)):
            for i in range (2):
                add = int (str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_x  += 1
    elif direction != True:
        temp_y = randint(2,10)
        temp_y -= 1
        temp_x = temp_y
        if (check_position_vertical(dictionary,temp_x,temp_y,2)):
            randomize_PatrolShip(dictionary)
        elif not(check_position_vertical(dictionary,temp_x,temp_y,2)):
            for i in range(2):
                add = int(str(temp_x) + str(temp_y))
                dictionary[add] = "ship"
                temp_y +=1
def printKeys(name,dictionary):
    if name == "admin":
        temp_x = 1
        temp_y = 0
        for i in range(10):
            temp_y += 1
            temp_x = 1
            for j in range(10):
                lkUp = int(str(temp_x) + str(temp_y))
                print("X: {} , Y: {} , VALUE: {}".format(temp_x,temp_y,(dictionary[lkUp])))
                temp_x += 1
    else:
        print ("Have Fun!")
def confirm_hitShip(dictionary,x,y):
    confirm = int(str(x) + str(y))
    if (dictionary[confirm]) == "ship":
        return True
    elif (dictionary[confirm]) == "empty":
        return False
def check_if_won(hit_count):
    if hit_count == 14:
        play_sound("victory")
        print("Nice job you Win")
        uWin= GraphWin(" YOU WIN!",350,350)
        uWin.setCoords(0,0,350,350)
        Intruc2 = Text(Point(200,335),("YOU CAN HAS WIN!"))
        Intruc2.draw(uWin)
        Intruc2.setSize(9)
        wins = Image(Point(175,175),"zomgwins.gif")
        wins.draw(uWin)
        uWin.getMouse()
        uWin.close()
        return True
def play_sound(identify):
    sound1 = pygame.mixer.Sound('miss.wav')
    sound2 = pygame.mixer.Sound('shiphit1.wav')
    sound3 = pygame.mixer.Sound('game.wav')
    sound4 = pygame.mixer.Sound('victory.wav')
    sound5 = pygame.mixer.Sound('loss1.wav')
    if identify == "miss":
        sound1.play()
    elif identify == "hit":
        sound2.play()
    elif identify == "game":
        sound3.play(-1)
    elif identify == "victory":
        sound4.play()
    elif identify == "loss":
        sound5.play()
    elif identify == "stop":
        pygame.mixer.stop()
def draw_menu(x1,y1,sizex,sizey,win):
    to_draw = Rectangle(Point(x1,y1),Point(sizex,sizey))
    to_draw.setOutline("white")
    to_draw.draw(win)
def get_difficulty():
    testW = GraphWin("Select Difficulty",900,300)
    testW.setCoords(0,0,900,300)

    for i in range(3):
        draw_menu(i*300,0,((i+1)*300),300,testW)
    Opt1 = Text(Point(150,150),("Easy"))
    Opt1.setSize(18)
    Opt1.draw(testW)

    Opt2 = Text(Point(450,150),("Normal"))
    Opt2.setSize(18)
    Opt2.draw(testW)

    Opt3 = Text(Point(750,150),("Hard"))
    Opt3.setSize(18)
    Opt3.draw(testW)

    try:
        center_point1 = testW.getMouse()
        center_p1x = int(center_point1.getX())
        var1 = 0
        if 0<center_p1x<301:
            choice = "easy"
            testW.close()
        elif 301<center_p1x<601:
            choice = "normal"
            testW.close()
        elif 601<center_p1x<900:
            choice = "hard"
            testW.close()
    except ValueError:
        print("What'd you do?!?!")
    return get_choice(choice)
def get_choice(choice):
    if choice == "easy":
        return 65
    elif choice == "normal":
        return 55
    elif choice == "hard":
        return 35
def check_if_lost(count, limit):
    if count == limit:
        play_sound("loss")
        print("LOL YOU LOSE NOOB")
        failWin= GraphWin(" YOU LOSE!",350,350)
        failWin.setCoords(0,0,350,350)
        Intruc2 = Text(Point(200,335),("YOU CAN HAS FAIL!"))
        Intruc2.draw(failWin)
        Intruc2.setSize(9)
        loss = Image(Point(175,175),"lose.gif")
        loss.draw(failWin)
        failWin.getMouse()
        failWin.close()
        return True
def if_already_clicked(lookUp,click):
  
    if((click[lookUp]) == "click"):
        confirm = True
    elif  ((click[lookUp]) != "click"):
        confirm = False
    click[lookUp] = "click"
    return confirm
def init_userClick_record():
    click ={ 11:"empty",12:"empty",13:"empty",14:"empty",15:"empty",
             16:"empty",17:"empty",18:"empty",19:"empty",110:"empty",           
             21:"empty",22:"empty",23:"empty",24:"empty",25:"empty",
             26:"empty",27:"empty",28:"empty",29:"empty",210:"empty",
             31:"empty",32:"empty",33:"empty",34:"empty",35:"empty",
             36:"empty",37:"empty",38:"empty",39:"empty",310:"empty",
             41:"empty",42:"empty",43:"empty",44:"empty",45:"empty",
             46:"empty",47:"empty",48:"empty",49:"empty",410:"empty",
             51:"empty",52:"empty",53:"empty",54:"empty",55:"empty",
             56:"empty",57:"empty",58:"empty",59:"empty",510:"empty",
             61:"empty",62:"empty",63:"empty",64:"empty",65:"empty",
             66:"empty",67:"empty",68:"empty",69:"empty",610:"empty",
             71:"empty",72:"empty",73:"empty",74:"empty",75:"empty",
             76:"empty",77:"empty",78:"empty",79:"empty",710:"empty",
             81:"empty",82:"empty",83:"empty",84:"empty",85:"empty",
             86:"empty",87:"empty",88:"empty",89:"empty",810:"empty",
             91:"empty",92:"empty",93:"empty",94:"empty",95:"empty",
             96:"empty",97:"empty",98:"empty",99:"empty",910:"empty",
             101:"empty",102:"empty",103:"empty",104:"empty",105:"empty",
             106:"empty",107:"empty",108:"empty",109:"empty",1010:"empty"}
    return click
print ("Welcome to BattleShip")
#init pygame.mixer for sounds
pygame.mixer.pre_init(44100,16,2,4096)
pygame.mixer.init()

#  Create Window and set coordinates
haxWin= GraphWin("Battleship",500,500)
haxWin.setCoords(0,0,500,500)

#  Draw Board
for j in range(10):
    for i in range(10):
        draw_sq(i*50, j*50,50,haxWin)
play_sound("game")
#  Instructions
print("Enter your Name")
name = raw_input("Enter: ")
#  Points are in (x, y)
#  Set Dictonary Values
hitDict={11:"empty",12:"empty",13:"empty",14:"empty",15:"empty",
         16:"empty",17:"empty",18:"empty",19:"empty",110:"empty",           
         21:"empty",22:"empty",23:"empty",24:"empty",25:"empty",
         26:"empty",27:"empty",28:"empty",29:"empty",210:"empty",
         31:"empty",32:"empty",33:"empty",34:"empty",35:"empty",
         36:"empty",37:"empty",38:"empty",39:"empty",310:"empty",
         41:"empty",42:"empty",43:"empty",44:"empty",45:"empty",
         46:"empty",47:"empty",48:"empty",49:"empty",410:"empty",
         51:"empty",52:"empty",53:"empty",54:"empty",55:"empty",
         56:"empty",57:"empty",58:"empty",59:"empty",510:"empty",
         61:"empty",62:"empty",63:"empty",64:"empty",65:"empty",
         66:"empty",67:"empty",68:"empty",69:"empty",610:"empty",
         71:"empty",72:"empty",73:"empty",74:"empty",75:"empty",
         76:"empty",77:"empty",78:"empty",79:"empty",710:"empty",
         81:"empty",82:"empty",83:"empty",84:"empty",85:"empty",
         86:"empty",87:"empty",88:"empty",89:"empty",810:"empty",
         91:"empty",92:"empty",93:"empty",94:"empty",95:"empty",
         96:"empty",97:"empty",98:"empty",99:"empty",910:"empty",
         101:"empty",102:"empty",103:"empty",104:"empty",105:"empty",
         106:"empty",107:"empty",108:"empty",109:"empty",1010:"empty"}


randomize_AircraftCarry(hitDict)
randomize_Submarine(hitDict)
randomize_Battleship(hitDict)
randomize_PatrolShip(hitDict)
printKeys(name,hitDict)
limit = get_difficulty()
users_clicks = init_userClick_record()
#  Get user mouse click and match with dictionary value
ask1 = 0
shipHit = 0
while ask1 <limit:
    try:
        #  Get user input, type cast to interger
        cenpt1= haxWin.getMouse()
        cen1x = int(cenpt1.getX())
        cen1y = int(cenpt1.getY())

        #approx midpoint for clean look
        var1 = 0
        
        if 0<cen1x<51:
            var1 += 1
            drawX = adjust(var1)
        elif 51<cen1x<99:
            var1 += 2
            drawX  = adjust(var1)
        elif 99<cen1x<149:
            var1 +=3
            drawX = adjust(var1)
        elif 149<cen1x<199:
            var1 += 4
            drawX = adjust(var1)
        elif 199<cen1x<249:
            var1 +=5
            drawX = adjust(var1)
        elif 249<cen1x <299:
            var1 += 6
            drawX = adjust(var1)
        elif 299<cen1x<349:
            var1 += 7
            drawX = adjust(var1)
        elif 349 <cen1x< 399:
            var1 += 8
            drawX = adjust(var1)
        elif 399<cen1x<449:
            var1 += 9
            drawX = adjust(var1)
        elif 449 < cen1x< 499:
            var1 += 10
            drawX = adjust(var1) 

        else:
            print("Sorry out of bounds")

        var2 = 0
       
        if 0<cen1y<51:
            var2 += 1
            drawY = adjust(var2)
        elif 51<cen1y<99:
            var2 += 2
            drawY = adjust(var2)
        elif 99<cen1y<149:
            var2 += 3
            drawY = adjust(var2)
        elif 149<cen1y<199:
            var2 += 4
            drawY = adjust(var2)
        elif 199<cen1y<249:
            var2 += 5
            drawY = adjust(var2)
        elif 249<cen1y <299:
            var2 += 6
            drawY = adjust(var2)
        elif 299<cen1y<349:  
            var2 += 7
            drawY = adjust(var2)
        elif 349 <cen1y< 399:
            var2 += 8
            drawY = adjust(var2)
        elif 399<cen1y<449:
            var2 += 9
            drawY = adjust(var2)
        elif 449 < cen1y< 499:
            var2 += 10
            drawY = adjust(var2) 
        else:
            print("Sorry out of bounds")
        
        lkUp = int(str(var1) + str(var2))
       
        if (if_already_clicked(lkUp,users_clicks)) == True:
            print("You have already clicked there, shot not counted!")
        else:
            target = (hitDict[lkUp])
            print(target)
            ask1 += 1
            
            if target == "empty":
                #draws an x for miss 
                play_sound("miss")
                missMark = Image(Point(drawX,drawY),"empty.gif")
                missMark.draw(haxWin)
            elif target == "ship":
                play_sound("hit")
                hitMark = Image(Point(drawX,drawY),"hit.gif")
                hitMark.draw(haxWin)
                shipHit +=1
            
            if (check_if_won(shipHit)):
                break
            elif (check_if_lost(ask1,limit)):      
                break
    except ValueError:
      print("Out of bounds")

                        
#  Close board window
haxWin.getMouse()
haxWin.close()

