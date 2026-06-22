#####################################################################################################
#Goose Around the World Animation
#Author: Asha
#Date: May 27, 2026
#####################################################################################################


#Initialize Tkinter with these
from tkinter import*
from time import *
from math import*
from random import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="white")
screen.pack()


#Your code goes here
#------------------------------------------------------------------------GENERAL BACKGROUND-------------------------------------------------------------------------------------------------------------------------------

#draw grass
grass = screen.create_rectangle(0,425,800,600,fill="#9AC20C", outline = "#9AC20C")

#draw sky
sky_height = 425
sky = screen.create_rectangle(0,0,800,sky_height, fill ="#98D5D6", outline = "#98D5D6")
    
    
#---------------------------------------------------------------------------------GOOSE---------------------------------------------------------------------------------------------------------------------------------------------------

#goose body anchor points
gx = 350
gy = 325

#draw body
body = screen.create_arc(gx,gy,gx+150,gy+150, start = 180, extent = 180,fill = "white", outline="", tags = "goose")

#goose neck angles & anchor points used later to rotate neck from vertical to horizontal
bottom_x = 380
bottom_y = 420
neck_height = 80
current_angle_neck = radians(-90)
target_angle_neck = radians(-180)
#draw neck
neck = screen.create_line(gx+20,gy+5,gx+20,gy+85, fill = "white", width = 40, tags = "goose")

#draw wing
wing = screen.create_arc(gx,gy+85,gx+100,gy+125,start = 270,extent = 180,fill ="white", outline = "black", tags = "goose")

#draw head and face
beak = screen.create_polygon(gx-20,gy+25,gx-50,gy+25,gx-10,gy-20,fill ="yellow",outline ="yellow", tags = "goose")
head = screen.create_arc(gx+40,gy-25,gx-30,gy+35,start=0,extent=359, fill = "white", outline="", tags = "goose")
eye = screen.create_oval(gx-5,gy-5,gx,gy+5,fill ="black",tags = "goose")

#left leg anchor points used later to rotate left leg
L_leg_x = gx+50
L_leg_y = gy+135
L_leg_x2 = gx+50
L_leg_y2 = gy+175
#draw left leg
L_leg = screen.create_line(gx+50,gy+135,gx+50,gy+175,fill = "yellow", width = 12, tags = "goose")

#right leg anchor points used later to rotate right leg
R_leg_x = gx+100
R_leg_y =gy+135
R_leg_x2 = gx+100
R_leg_y2 = gy+175
#draw right leg
R_leg = screen.create_line(gx+100,gy+135,gx+100,gy+175, fill = "yellow", width = 12, tags = "goose")


#create a rotation function to shift the goose's neck into a horizontal position
def rotate(bx,by,line_length, angle):
     
    #rotate the line in using a circle
    x2 = bx +line_length*cos(angle)
    y2 = by +line_length*sin(angle)
    
    #return the calculated x and y endpoints
    return x2,y2


#--------------------------------------------------------------------------Animation Loop 1: Lift Off!!!!!!!!!!------------------------------------------------------------------------------------------------

#MAIN ANIMATION: Goose lifting off
for frames in range(110):

    #lower sky down 
    sky_height = sky_height + 2
    sky = screen.create_rectangle(0,0,800,sky_height, fill ="#98D5D6", outline = "")
    
    #ensure that the grass and the sky are behind the goose in the background
    screen.tag_lower(sky)
    screen.tag_lower(grass)
    
    
    #lift goose into flying position
    gy  -=1.5
    
    #shift goose's neck into flying position
    if current_angle_neck > target_angle_neck:
        current_angle_neck -=0.02
    #move neck upward
    bottom_y =gy+95
    #calculate neck ending point from body (where it attaches to the head)
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    
    #draw goose's neck using the calculate endpoints
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    
    
    #shift goose legs into flying position
    #left leg
    L_leg_x +=0.35
    L_leg_y -=1.44
    L_leg_x2+=0.85
    L_leg_y2 -=1.28
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #right leg
    R_leg_x +=0.15
    R_leg_y -=1.52
    R_leg_x2+=0.54
    R_leg_y2 -=1.54
    
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")
    
    
    #shift goose body into flying position
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    
    #update screen to show each new frame
    screen.update()
    #pause code temporarily to see each updated frame
    sleep(0.0333)
    
    #delete previous goose frame to show the newest one
    screen.delete("goose")
    
  
    
#------------------------------------------------------------------------------------------------Animation Loop 2: Goose Flying------------------------------------------------------------------------------------------------------------

#MAIN ANIMATION: Goose flying
for frames in range(170):
    #delete the previous goose to show the most recently drawn goose frame
    screen.delete("goose")
    
    #flying path for goose to oscilate up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop  flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen so you can see each  new frame
    screen.update()
    
    #pause code temporarily to show each updated frame
    sleep(0.0333)
    

#-----------------------------------------------------------------------------Animation Loop 3: In Paris------------------------------------------------------------------------------------------------------------------------    

#PARIS Background
#land
grass = screen.create_rectangle(0,450,800,600,fill ="#9AC20C", outline ="", tags="paris")
sidewalk = screen.create_polygon(375,450,0,575,0,600,800,600,800,575,625,450, fill = "#949391", outline ="", tags="paris")
road = screen.create_polygon(100,600, 450,450,550, 450,700,600, fill = "#787774", outline = "", tags ="paris")
sidewalk_shadow = screen.create_line(450,450,110,600,100,800,700,800,700,600,550,450,fill = "gray", width = 10, tags ="paris")


#Eiffel Tower
bottom_third = screen.create_polygon(400,450,425,375,575,375,600,450, fill = "#B09E7B", outline ="", tags ="paris")
blue_arc = screen.create_arc(450,400,550,500,start =0,extent=180,fill ="#98D5D6",outline="",tags="paris")
bottom_divider = screen.create_rectangle(420,360,580,375, fill ="#B09E7B", outline ="#8F8064",tags ="paris")
middle_third = screen.create_polygon(435,360,465,250,535,250,565,360,fill = "#B09E7B", outline ="", tags ="paris")
blue_trapezoid = screen.create_polygon(465,360,485,270,515,270,535,360, fill ="#98D5D6", outline ="", tags = "paris")
middle_divider = screen.create_rectangle(460,235,540,250,fill ="#B09E7B",outline="#8F8064", tags = "paris")
top_third = screen.create_polygon(475,235,485,100,500,70,515,100,525,235,fill ="#B09E7B", outline = "", tags ="paris")


#left side hedges
L_hedge_height = 100
L_hedge_width = 80

#draw hedges along the sidewalk
for Lx in range(-30,230,60):
    #set hedge boundary along the line between the sidewalk and the grass 
    L_boundary_y = -Lx/3 +575
    
    L_hedge_y = L_boundary_y - L_hedge_height
    
    L_hedge = screen.create_arc(Lx,L_hedge_y,Lx+L_hedge_width,L_boundary_y, start = 0,extent =180,fill ="#90AD21", outline ="", tags ="paris")
    
    #calculate the center of the hedge circles
    L_hedge_center_x = Lx + L_hedge_width/2
    L_hedge_center_y = L_boundary_y - L_hedge_height/2
    
    #add randomly placed flowers to the hedges
    for i in range(5):
        L_flower_y = randint(int(L_hedge_y +5),int(L_hedge_center_y-8))
        L_flower_x = randint(int(Lx+8), int (Lx+L_hedge_width-13))
        L_flower = screen.create_oval(L_flower_x,L_flower_y,L_flower_x+8,L_flower_y+8,fill = "#FA2D6B",outline = "", tags = "paris")
    


#right side hedges
R_hedge_height = 100
R_hedge_width =80

#draw hedges along the sidewalk
for Rx in range(700,900,50):
    #set hedge boundary along the line between the sidwalk and the grass
    R_boundary_y = (125/175)*Rx+3.6
    
    R_hedge_y = R_boundary_y - R_hedge_height
    
    R_hedge = screen.create_arc(Rx,R_hedge_y,Rx+R_hedge_width,R_boundary_y, start = 0,extent =180,fill ="#90AD21", outline ="", tags="paris")
    
    #calculate the center of the hedge circles
    R_hedge_center_x = Rx + R_hedge_width/2
    R_hedge_center_y = R_boundary_y - R_hedge_height/2
    
    #add randomly placed flowers to the hedges
    for i in range(5):
        R_flower_y = randint(int(R_hedge_y +5),int (R_hedge_center_y-8))
        R_flower_x = randint(int(Rx+8),int(Rx+R_hedge_width-13))
        R_flower = screen.create_oval(R_flower_x,R_flower_y,R_flower_x+8,R_flower_y+8,fill = "#FA2D6B",outline = "", tags ="paris")
    


#clouds anchor points
xcloud = 50
ycloud = 80

xcloud2 = 600
ycloud2 = 250

#MAIN ANIMATION: Goose flying + Clouds drifting
for frames in range(352):
    
    #delete the previous goose frame to show the most recent goose frame
    screen.delete("goose")
    
    #cloud 1
    cloud_L = screen.create_oval(xcloud,ycloud,xcloud+75,ycloud+70,fill = "#B8DEDE", outline ="", tags ="cloud1")
    cloud_R = screen.create_oval(xcloud+120,ycloud,xcloud+195,ycloud+70, fill ="#B8DEDE", outline ="", tags = "cloud1")
    cloud_middle = screen.create_oval(xcloud+50,ycloud-30,xcloud+150,ycloud+70, fill ="#B8DEDE", outline ="", tags = "cloud1")
    
    xcloud+=0.4
    
    #cloud 2
    cloud_L = screen.create_oval(xcloud2,ycloud2,xcloud2+75,ycloud2+50,fill = "#B8DEDE", outline ="", tags = "cloud2")
    cloud_R = screen.create_oval(xcloud2+75,ycloud2,xcloud2+150,ycloud2+50, fill ="#B8DEDE", outline ="", tags ="cloud2")
    cloud_middle = screen.create_oval(xcloud2+40,ycloud2-20,xcloud2+110,ycloud2+50, fill ="#B8DEDE", outline ="",tags = "cloud2")

    xcloud2-=0.2
    
    
    #flying path for goose to oscillate  up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen to show each new frame
    screen.update()
    
    #pause code temporarily to see each updated frame
    sleep(0.0333)
    
    #delete the old cloud frame to show the newest cloud frame
    screen.delete("cloud1", "cloud2")





#-------------------------------------------------------------------------Animation Loop 4: In Egypt---------------------------------------------------------------------------------------------------------------------------------

#EGYPT background

#pyramids
smaller_pyramid = screen.create_polygon(600,450,725,280,900,450, fill ="#E8C861", outline ="", tags = "egypt")
big_pyramid = screen.create_polygon(330,480,540,200,750,480, fill = "#FAD766", outline ="", tags ="egypt")

#sand hills
back_hill = screen.create_polygon(-100,460,150,450,300,440,400,455,450,465,800,475,800,600,-100,600, fill = "#CC9E47", outline ="", smooth = True, tags="egypt")
front_hill = screen.create_polygon(-100,500,200,525,500,500,600,450,650,435,900,430,900,900,0,900,fill ="#EBB552", outline ="", smooth =True, tags = "egypt")

#sun
sun = screen.create_oval(150,100,250,200, fill ="#FFDB2E", outline ="", tags ="egypt")


#camel
camel_body = screen.create_oval(200,470,260,500, fill ="#9E7B23", outline ="", tags = "camel")
L_camel_leg = screen.create_line(215,490,215,520, fill ="#9E7B23", width = 8, tags ="camel")
R_camel_leg = screen.create_line(245, 490,245,520, fill ="#9E7B23", width =8, tags ="camel")

camel_neck = screen.create_line(205,480,205,450, fill ="#9E7B23", width = 10, tags = "camel")

camel_head = screen.create_line(210,448,190,448, fill ="#9E7B23", width = 12, tags = "camel")
camel_ear = screen.create_oval (218,440,205,446, fill ="#9E7B23", outline = "", tags ="camel")
camel_eye = screen.create_oval(200,445,205,450,fill ="#4F3D11", outline="", tags ="camel")

camel_hump1 = screen.create_arc(215,450,230,510, start = 0, extent = 180, fill ="#9E7B23", outline ="", tags ="camel")
camel_hump2 = screen.create_arc(230,455,250,520,start = 0, extent = 180, fill ="#9E7B23", outline ="", tags = "camel")


#MAIN ANIMATION: Goose flying
for frames in range(352):
    
    #delete previous scene
    screen.delete("paris")
    
    #animate goose
    screen.delete("goose")
    
        #flying path for goose to oscilate up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop  flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen to show each new frame
    screen.update()
    
    #pause code temporarily to see each frame
    sleep(0.0333)
    





#-------------------------------------------------------------------------------Animation Loop 5: In NYC----------------------------------------------------------------------------------------------------------------------

#NEW YORK Background

#ocean
ocean = screen.create_rectangle(0,400,800,600, fill ="#537F8C", outline ="", tags ="nyc")


#building 
building1_x = 800
building1_width = randrange(20,50,10)

while building1_x-building1_width > 350:
    
    building1_y = randrange(280,370,10)
    height1 = 400-building1_y

    building1 = screen.create_rectangle(building1_x,building1_y,building1_x-building1_width,building1_y+height1, fill ="#668891", outline ="#5B7A82", tags="nyc", width =2)

    building1_x -=building1_width
    building1_width = randrange(20,50,10)
    


#land
land = screen.create_polygon(800,400,350,400,330,410,320,420,800,420, fill ="#8BA154", outline ="", tags ="nyc")


#STATUE OF LIBERTY (SoL)
#SoL base
green_base = screen.create_rectangle(50,560,300,600, fill ="#629680", outline ="#568571", tags = "statue", width = 2)
tan_base = screen.create_line(25,600,325,600, fill ="#C7AB63", width = 25, tags ="statue")


#SoL right arm
right_arm = screen.create_polygon(240,240,300,350,240,350, fill ="#629680", outline ="#568571", tags = "statue", width = 2)
book = screen.create_polygon(250,315,275,280,320,320,255,390, fill ="#568571", outline ="#568571", width =2, tags = "statue")
right_hand = screen.create_arc(265,340,315,390, start = 40, extent = 180,fill ="#629680", outline ="#568571", width =2, tags ="statue")


#SoL left armm
left_arm = screen.create_polygon(65,175,45,130,25,130,45,210,fill ="#629680", tags ="statue")
torch = screen.create_polygon(33,160,50,160,50,120,70,105,13,105,33,120, fill ="#568571", outline ="#568571", tags ="statue", width =2)
fire = screen.create_polygon(28,100,42,105,55,100, 42,70,fill ="#568571", outline ="", tags ="statue", smooth =True)


#SoL head + neck
hair = screen.create_polygon(110,250,110,250,115,110,175,90,225,105,230,125,235,300, fill ="#629680", outline ="#568571", width = 2, smooth = True, tags ="statue")

spikes = screen.create_polygon(125,110,115,75,150,100,155,60,175,95,195,60,200,110,210,95,235,70,230,110, fill ="#629680", outline ="", tags ="statue")
headband = screen.create_line(125,110,150,100,175,90,200,100,225,110, fill ="#568571", width = 7, smooth = True, tags ="statue")


statue_neck = screen.create_line(160,200,150,240, width = 2, fill ="#568571", tags = "statue")
statue_neck =screen.create_line(190,200,200,240, fill = "#568571", width =2, tags ="statue")

face = screen.create_line(130,145,150,200,175,210,200,200,220,145, fill ="#568571", tags = "statue", width =2, smooth =True)


bangs = screen.create_line(125,142,150,150,175,125,200,150,225,142, fill ="#568571", width = 2, smooth =True, tags ="statue")


#SoL clothes
dress_layer1 = screen.create_polygon(75,560,80,470,250,410,275,560, fill ="#629680", outline ="", tags = "statue")

shoulder = screen.create_polygon(220,240,220,300,115,290,40,220,65,175,130,240, fill ="#629680", outline = "#568571", tags = "statue")

dress_layer3 = screen.create_polygon(220,250,100,290,90,350,85,350,65,480,240,480, fill ="#629680", outline = "#568571", width = 2, tags ="statue")

dress_layer2 = screen.create_polygon(65,525,140,525,240,480,250,430,250,510,280,530,240,230,220,240,190,400,75,470, fill ="#629680", outline ="#568571", width = 2, tags = "statue")

screen.create_line(85,350,170,300, fill ="#568571", width = 2, tags ="statue")



#MAIN ANIMATION: Goose flying
for frames in range(352):
    
    #delete previous scene
    screen.delete("camel","egypt")
    
    #animate goose
    screen.delete("goose")
    
        #flying path for goose to oscilate up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen to show each new frame
    screen.update()
    
    #pause code temporarily to see each frame
    sleep(0.0333)
    



#----------------------------------------------------------------------Animation Loop 6: Loop the Loop-------------------------------------------------------------------------------------------------


#MAIN ANIMATION: Goose Flying Motion
for frames in range(95):
    
    #delete previous scene
    screen.delete("nyc","statue")
    
    #animate goose
    screen.delete("goose")
    
        #flying path for goose to oscilate up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen so you can see each frame
    screen.update()
    
    #pause code temporarily to render each frame
    sleep(0.0333)



#Loop the Loop
#loop parameters
loop_x = 420
loop_y = 120
loop_radius = 100
loop_angle = 0
loop_angle_step = 0.15

#MAIN ANIMATION: Loop the Loop
for frames in range(50):
    screen.delete("nyc", "statue", "goose")
    
    #move goose left 
    loop_x -=3
    
    #move the goose in a circular loop shape
    gx = loop_x + loop_radius * cos(loop_angle)
    gy = loop_y + loop_radius * sin(loop_angle)
    
    #increase the angle of the loop each frame
    loop_angle += loop_angle_step
    
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen to show each individual frame
    screen.update()
    
    #pause code temporarily to see the frame
    sleep(0.03333)
    


#MAIN ANIMATION: Goose Flying Motion
for frames in range(158):
    
    #delete previous scene
    screen.delete("nyc","statue")
    
    #ANIMATE GOOSE
    screen.delete("goose")
    
        #flying path for goose to oscilate  up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900
        
        
    #draw the goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw the goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen so you can see each frame
    screen.update()
    
    #pause code temporarily to render each frame
    sleep(0.0333)


#-------------------------------------------------------------------------Animation Loop 7: Goose Crashes---------------------------------------------------------------------------------------------------------------

#brick wall
wall = screen.create_rectangle(0,0,300,600, fill ="#A6663C", outline ="", tags = "building")

#window
bottom_window = screen.create_polygon(100,550,250,530,250,700,100,700, fill ="#B0CED6", outline = "white", width =6, tags ="building")
top_window = screen.create_polygon(100,50,250,70,250,-100,100,-100, fill ="#B0CED6", outline ="white", width =6, tags = "building")

window = screen.create_polygon(100,150,250,170,250,430,100,450, fill = "#B0CED6", outline ="white", width = 6, tags = "buidling")
vertical_line = screen.create_line(175,160,175,440, fill ="white", width = 5, tags ="building")
horizontal_line = screen.create_line(100,295,250,305, fill ="white", width =5, tags = "building")


#MAIN  ANIMATION: Goose neck snaps
for frames in range(215):
    
    #hitting the wall effects
    if frames>=213:
       hit_effect = screen.create_line(160,240,180,145,150,230,130,180,140,250,115,255,130,270,120,275,130,290,105,320,150,305,220,380,180,300, fill ="red", width = 4, tags ="building")
       effect_line1 = screen.create_line(185,230,195,210,fill ="red", width = 4, tags ="building")
       effect_line2 = screen.create_line(175,250,220,230, fill ="red", width =4, tags ="building" )
    
    
    #delete previous scene
    screen.delete("nyc","statue")
    
    #animate goose
    screen.delete("goose")
    
    #flying path for goose to oscilate y up and down
    gy = 8*sin (0.25*frames)+160
    
    #loop flying so it wraps around
    if gx > -150:
        gx -=3
    else:
        gx = 900

    #quickly change the goose's neck angle to make it snap down
    if frames >=214:
        current_angle_neck = radians(150)
    else:
        current_angle_neck = radians (-180)
        
    #draw the goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    
    #draw the dead goose eye when the goose hits the window
    if frames >= 214:
        eye = screen.create_line(head_x-5, head_y+2, head_x+5, head_y-10, fill ="black", width = 3,tags = "goose")
        eye = screen.create_line(head_x+5, head_y+2, head_x-5, head_y-10, fill ="black", width = 3,tags = "goose")
    else:    
        eye = screen.create_oval(head_x-10,head_y-10,head_x-5,head_y, fill ="black",tags = "goose")
    
    
    
    #draw goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw the goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen so you can see each frame
    screen.update()
    
    #pause code temporarily to render each frame
    sleep(0.0333)




#MAIN  ANIMATION: Goose falling down animation
for frames in range(58):

    #delete previous scene
    screen.delete("nyc","statue")
    
    #ANIMATE GOOSE
    screen.delete("goose")
    
    #flying path to drop y and make the goose look like it's falling
    gy +=9

        
    #draw the goose's neck
    bottom_y = gy +95
    bottom_x = gx+30
    head_x, head_y = rotate(bottom_x, bottom_y,neck_height,current_angle_neck)
    neck = screen.create_line(bottom_x,bottom_y,head_x,head_y, fill ="white", width = 40, tags = "goose")
    
    #attatch goose's head, eyes, beak to neck
    head = screen.create_oval(head_x -35,head_y-35,head_x+35,head_y+35, fill = "white", outline = "" ,tags = "goose")
    beak = screen.create_polygon(head_x-25,head_y+20,head_x-65,head_y+20,head_x-25,head_y-20,fill = "yellow",outline ="",tags = "goose")
    eye = screen.create_line(head_x-5, head_y+2, head_x+5, head_y-10, fill ="black", width = 3,tags = "goose")
    eye = screen.create_line(head_x+5, head_y+2, head_x-5, head_y-10, fill ="black", width = 3,tags = "goose")
        
    #draw the goose's left leg
    L_leg_x = gx+88.5
    L_leg_y = gy + 140
    L_leg_x2 = gx+143.5
    L_leg_y2 = gy  +180
    
    L_leg = screen.create_line(L_leg_x,L_leg_y,L_leg_x2,L_leg_y2, fill ="yellow", width =12, tags = "goose")
    
    #draw the goose's right leg
    R_leg_x = gx +116.5
    R_leg_y = gy +120
    R_leg_x2 = gx +159.5
    R_leg_y2 = gy +140
    
    R_leg = screen.create_line(R_leg_x,R_leg_y,R_leg_x2,R_leg_y2, fill = "yellow", width = 12, tags = "goose")

    #draw the goose's body
    body = screen.create_arc(gx, gy,gx + 150, gy + 150, start=180,extent=180,fill="white",outline="",tags="goose")
    wing = screen.create_arc( gx,gy + 85,gx + 100,gy + 125,start=270,extent=180,fill="white",outline="black",tags="goose")
   
    #update screen to show each individual frame
    screen.update()
    
    #pause code temporarily to be able to see each frame
    sleep(0.0333)





#--------------------------------------------------------------------------------------------------------------------------------------
#


#Grid lines
#REMOVE THESE BEFORE SUBMITTING ANY ASSIGNMENTS
spacing = 50

for x in range(0, 800, spacing): 
    screen.create_line(x, 25, x, 600, fill="white")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

for y in range(0, 600, spacing):
    screen.create_line(25, y, 800, y, fill="white")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")

screen.mainloop()
